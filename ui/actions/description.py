"""UI description actions."""
import typing as t

fetch: t.Any = 0  # __:skip


def draw_description(state, description: str):
    """Draw description."""
    return {"content": description}


async def fetch_description(state, actions):
    """Fetch description as HTML."""
    response = await fetch(f"/description", {"method": "GET"})
    if not response.ok:
        raise Exception(f"{response.status}: {response.text()}")
    description: str = await response.text()
    actions["draw_description"](description)


def description_actions() -> t.Dict[str, t.Callable]:
    """UI description actions."""
    return {
        "draw_description": lambda description: lambda state: draw_description(
            state, description
        ),
        "fetch_description": lambda data: lambda state, actions: fetch_description(
            state, actions
        ),
    }
