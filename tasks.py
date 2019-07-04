#!/usr/bin/env python3.7
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
    cwd = os.getcwd()
    if cwd.startswith("/mnt/c"):
        cwd = re.sub("^/mnt", "", cwd)
    return subprocess.run(
        fr"""
        docker run \
            -v {quote(cwd)}:/data:cached \
            --rm \
            {docker_options} \
            martian_imperial_year_table:development {command}
        """,
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
    if not within_docker():
        run(
            r"""
            docker build \
                -f deployments/development/Dockerfile \
                -t martian_imperial_year_table:development \
                --force-rm \
                --pull \
                .
            """
        )
    setup()
    run("mkdir -p static/css static/js")
    run("cp node_modules/bulma/css/* static/css/")
    with docker() as _run:
        _run("pipenv run transcrypt -b -m -n ui_main.py")
    run("mv __target__/* static/js/")


@task
def clean():
    """Clean built files."""
    run("rm -rf __target__ static/css static/js")


@task
def deploy_staging():
    """Deploy to staging."""
    with powershell() as _run:
        _run(
            r"""
            kubectl apply \
                -n staging \
                --prune \
                --selector app=martian-imperial-year-table \
                -k deployments\staging
            """
        )
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
        _run("kubectl -n staging get ev -w --sort-by '.metadata.creationTimestamp'")


@task
def deploy_production():
    """Deploy to production."""
    with powershell() as _run:
        _run(
            r"""
            kubectl apply \
                -n default \
                --prune \
                --selector app=martian-imperial-year-table \
                -k deployments\production
            """
        )
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
        _run("kubectl -n default get ev -w --sort-by '.metadata.creationTimestamp'")


@task
def format():
    """Format code."""
    run(r"ag -l '\r' | xargs -r -t sed -i -e 's/\r//'")
    with docker() as _run:
        _run("pipenv run black *.py imperial_calendar tests ui")
        _run("node_modules/.bin/prettier --write README.md")


@task
def setup():
    """Install deps."""
    with docker() as _run:
        _run("pipenv install -d")
        _run("npm install")


@task
def sh():
    """Run shell in docker."""
    with docker() as _run:
        _run("sh", "-it")


@task
def start():
    """Start dev server."""
    with docker() as _run:
        _run("", "-p 0.0.0.0:5000:5000")


def test():
    """Test."""
    with docker() as _run:
        _run("pipenv check || true")
        _run("npm audit")
        _run(r"ag --hidden -g '\.ya?ml$' | xargs -r -t pipenv run yamllint")
        _run("hadolint deployments/*/Dockerfile")
        _run("pipenv run black --check *.py imperial_calendar tests ui")
        _run("pipenv run flake8 .")
        _run("pipenv run mypy debug.py")
        _run("pipenv run python -m unittest discover -s tests/imperial_calendar")
        _run(
            "pipenv run python -m unittest discover -s tests/imperial_calendar/internal"
        )
        _run(
            "pipenv run python -m unittest discover -s tests/imperial_calendar/transform"
        )


if len(sys.argv) == 1 or sys.argv[1] == "help":
    for task_name, describe in tasks.items():
        print(f"{task_name.ljust(16)}\t{describe}")
    exit
for task_name in sys.argv[1:]:
    locals()[task_name]()
