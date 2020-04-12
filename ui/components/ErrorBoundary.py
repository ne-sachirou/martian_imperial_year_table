"""ErrorBoundary component."""
import typing as t

React: t.Any = 0  # __:skip
console: t.Any = 0  # __:skip
createReactClass: t.Any = 0  # __:skip


def renderErrorBoundary():
    """Render a component."""
    this: t.Any = 0  # __:skip
    if this.state.has_error:
        return React.createElement("a", {"href": "/"}, "Reload")
    return this.props.children


ErrorBoundary = createReactClass(
    {
        "componentDidCatch": lambda error, errorInfo: console.error(error, errorInfo),
        "displayName": "ErrorBoundary",
        "getInitialState": lambda: {"has_error": False},
        "render": renderErrorBoundary,
        "statics": {"getDerivedStateFromError": lambda error: {"has_error": True}},
    }
)


def supervise(*children):
    """Supervise children components & give a fallback UI."""
    return React.createElement(ErrorBoundary, {}, *children)
