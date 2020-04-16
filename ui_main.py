"""Main."""
from ui.components.App import App
import typing as t

React: t.Any = 0  # __:skip
ReactDOM: t.Any = 0  # __:skip
document: t.Any = 0  # __:skip
window: t.Any = 0  # __:skip

if __name__ == "__main__":
    window.addEventListener(
        "DOMContentLoaded",
        lambda event: ReactDOM.render(
            React.createElement(App, {}), document.getElementById("app")
        ),
    )
