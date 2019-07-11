"""UI actions."""
import typing as t
from ui.actions.description import description_actions
from ui.actions.global_navigation import global_navigation_actions
from ui.actions.transform import transform_actions


def actions() -> t.Dict[str, t.Dict[str, t.Callable]]:
    """Actions."""
    return {
        "description": description_actions(),
        "global_navigation": global_navigation_actions(),
        "transform": transform_actions(),
    }


__all__ = ["actions"]
