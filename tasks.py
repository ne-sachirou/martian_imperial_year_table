#!/usr/bin/env python3.8
"""
Tasks.

cf. Welcome to Invoke! — Invoke documentation https://www.pyinvoke.org/
"""
from contextlib import contextmanager
import os
import os.path
import re
from shlex import quote
import subprocess
import sys
import time

tasks = {}


@contextmanager
def docker():
    """Run command in Docker."""
    if within_docker():
        yield run
    else:
        yield run_in_docker


@contextmanager
def powershell():
    """Run command in PowerShell if it's present."""
    if within_wsl():
        yield run_in_powershell
    else:
        yield run


def run(command: str, capture_output=False, text=None) -> subprocess.CompletedProcess:
    """Run command."""
    command = command.strip()
    print(command)
    return subprocess.run(
        command, capture_output=capture_output, check=True, shell=True, text=text
    )


def run_in_docker(
    command: str, docker_options="", capture_output=False, text=None
) -> subprocess.CompletedProcess:
    """Run command in Docker."""
    command = command.strip()
    print(command)
    # cwd = os.getcwd()
    # if cwd.startswith("/mnt/c"):
    #     cwd = re.sub("^/mnt", "", cwd)
    return subprocess.run(
        fr"""
        docker-compose {docker_options} run --rm web {command}
        """,
        # fr"""
        # docker run \
        #     -v {quote(cwd)}:/mnt:cached \
        #     --rm \
        #     {docker_options} \
        #     martian_imperial_year_table:development {command}
        # """,
        capture_output=capture_output,
        check=True,
        shell=True,
        text=text,
    )


def run_in_powershell(
    command: str, capture_output=False, text=None
) -> subprocess.CompletedProcess:
    """Run command in PowerShell if it's present."""
    command = re.sub(r"\\\n", r"`\n", command.strip())
    print(command)
    return subprocess.run(
        f"powershell.exe -Command {quote(command)}",
        capture_output=capture_output,
        check=True,
        shell=True,
        text=text,
    )


def task(function):
    """Define a task."""
    if function.__doc__:
        tasks[function.__name__] = function.__doc__

    def wrapper():
        function()

    return wrapper


def within_docker() -> bool:
    """Detect I'm in a Docker or not."""
    return os.path.exists("/.dockerenv") or os.getenv("CI") == "1"


def within_wsl() -> bool:
    """Detect I'm in a WSL or not."""
    return os.popen("which powershell.exe").read() != ""


@task
def build():
    """Build."""
    run("mkdir -p static/css static/js")
    if not within_docker():
        run("docker-compose pull web-src")
        run(
            r"""
            docker-compose build \
              --build-arg BUILDKIT_INLINE_CACHE=1 \
              --force-rm \
              --parallel \
              --pull
            """
        )
        run("docker-compose run --rm web-src /docker-entrypoint.d/precopy_appsync.sh")
    with docker() as _run:
        _run(
            "sh -eux -c {:s}".format(quote(r"cp node_modules/bulma/css/* static/css/"))
        )
        _run("poetry run npx webpack")
        _run("sh -eux -c {:s}".format(quote(r"mv dist/* static/js/")))


@task
def clean():
    """Clean built files."""
    if not within_docker():
        run("docker-compose down -v")
    run("rm -rfv static/css static/js")
    run("rm -rfv __target__ node_modules")


@task
def deploy_staging():
    """Deploy to staging."""
    run("git tag -f staging")
    run("git push -f origin staging")
    with powershell() as _run:
        time.sleep(10)
        builds_filter = r"""
        source.repoSource.repoName = github_ne-sachirou_martian_imperial_year_table AND
        source.repoSource.tagName = staging
        """.strip().replace(
            "\n", " "
        )
        process = _run(
            f"gcloud builds list --filter {quote(builds_filter)} --limit 1",
            capture_output=True,
            text=True,
        )
        build = process.stdout.split("\n")[1].split(" ")[0]
        _run(f"gcloud builds log --stream {quote(build)}")


@task
def deploy_production():
    """Deploy to production."""
    run("git tag -f production")
    run("git push -f origin production")
    with powershell() as _run:
        time.sleep(10)
        builds_filter = r"""
        source.repoSource.repoName = github_ne-sachirou_martian_imperial_year_table AND
        source.repoSource.tagName = production
        """.strip().replace(
            "\n", " "
        )
        process = _run(
            f"gcloud builds list --filter {quote(builds_filter)} --limit 1",
            capture_output=True,
            text=True,
        )
        build = process.stdout.split("\n")[1].split(" ")[0]
        _run(f"gcloud builds log --stream {quote(build)}")


@task
def format():
    """Format code."""
    run(r"ag -l '\r' | xargs -t -I{} sed -i -e 's/\r//' {}")
    with docker() as _run:
        _run("poetry run black *.py imperial_calendar tests ui")
        _run("npx prettier --write README.md templates/*.md")
        _run("npx prettier --write *.js")
        _run(
            "sh -eux -c {:s}".format(
                quote(
                    r"ag --hidden -g \.ya?ml$ | xargs -t npx prettier --parser yaml --write"
                )
            )
        )


@task
def sh():
    """Run shell in docker."""
    with docker() as _run:
        _run("sh")


@task
def start():
    """Start dev server."""
    run("docker-compose up")


@task
def test():
    """Test."""
    if not within_docker():
        for env in ["development", "staging"]:
            run(
                fr"""
               docker run -i \
                 -v $(pwd):/mnt \
                 --rm \
                 hadolint/hadolint \
                 hadolint \
                   --config /mnt/.hadolint.yaml \
                   /mnt/deployments/{env}/Dockerfile
               """
            )
    with docker() as _run:
        _run("poetry check")
        _run("npm audit")
        # _run(
        #     "sh -eux -c {:s}".format(
        #         quote(r"ag --hidden -g \.ya?ml$ | xargs -t poetry run yamllint")
        #     )
        # )
        _run("poetry run black --check *.py imperial_calendar tests ui")
        _run("poetry run flake8 .")
        _run("poetry run mypy debug.py")
        _run("poetry run python -m unittest discover -s tests/imperial_calendar")
        _run("poetry run python -m unittest discover -s tests/web")


@task
def upgrade():
    """Upgrade dependencies."""
    with docker() as _run:
        _run("npx npm-check-updates -u")
        _run("npm install")
        _run("npm audit fix")
        _run("npm fund")
        _run("poetry update")


if len(sys.argv) == 1 or sys.argv[1] == "help":
    for task_name, describe in tasks.items():
        print(f"{task_name.ljust(16)}\t{describe}")
    exit(0)
for task_name in sys.argv[1:]:
    locals()[task_name]()
