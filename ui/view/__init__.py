"""UI view."""
from node_modules.hyperapp.src.index import h  # type: ignore
from ui.view.description import view_description
from ui.view.global_navigation import view_global_navigation
from ui.view.transform import view_transform


def view(state, actions):
    """UI View."""
    main_content = state["global_navigation"]["main_content"]
    if main_content == "transform":
        view_main_content = view_transform
    elif main_content == "description":
        view_main_content = view_description
    else:
        raise Exception(f"Unknown main_content view: {main_content}")
    return h("div", {}, [view_global_navigation, view_main_content])


__all__ = ["view"]
