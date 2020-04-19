"""Root React component."""
from ui.components.Description import Description
from ui.components.ErrorBoundary import supervise
from ui.components.GlobalNavigation import GlobalNavigation
from ui.components.Transform import Transform
import typing as t

__pragma__(  # noqa: F821
    "js",
    "{}",
    """
    const React = require("react");
    const ReactRouterDOM = require("react-router-dom");
    """,
)

React: t.Any = 0  # __:skip
ReactRouterDOM: t.Any = 0  # __:skip


def App(props):
    """Root React component."""
    return supervise(
        React.createElement(
            ReactRouterDOM.BrowserRouter,
            {},
            supervise(React.createElement(GlobalNavigation, {})),
            supervise(
                React.createElement(
                    ReactRouterDOM.Switch,
                    {},
                    React.createElement(
                        ReactRouterDOM.Route,
                        {"path": "/", "exact": None},
                        React.createElement(Transform, {}),
                    ),
                    React.createElement(
                        ReactRouterDOM.Route,
                        {"path": "/description"},
                        React.createElement(Description, {}),
                    ),
                ),
            ),
        ),
    )
