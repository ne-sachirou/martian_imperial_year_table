"""UI global navigation actions."""
import typing as t


def switch_main_content(state, event):
    """Switch main content."""
    event.stopPropagation()
    event.preventDefault()
    return {"is_active": False, "main_content": event.target.dataset.mainContent}


def toggle_navbar_menu(state, event):
    """Toggle navbar menu."""
    event.stopPropagation()
    event.preventDefault()
    return {"is_active": not state["is_active"]}


def global_navigation_actions() -> t.Dict[str, t.Callable]:
    """UI global navigation actions."""
    return {
        "switch_main_content": lambda event: lambda state: switch_main_content(
            state, event
        ),
        "toggle_navbar_menu": lambda event: lambda state: toggle_navbar_menu(
            state, event
        ),
    }
