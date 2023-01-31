# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FlexLayout(Component):
    """A FlexLayout component.
Component description

Keyword arguments:

- children (a list of or a singular dash component, string or number; required):
    List of children to be rendered. Children are allocated to their
    respective tab based on the ID of the element.  WARNING: There is
    no validation done on whether the children here will be rendered
    in any tab. If there is no matching tab for a particular ID, that
    element will be silently ignored in rendering (although callbacks
    will still be applied).

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- debugMode (boolean; optional)

- font (boolean | number | string | dict | list; optional):
    the tab font (overrides value in css). Example:
    font={{size:\"12px\", style:\"italic\"}}.

- headers (dict; optional):
    Map of headers to render for each tab. Uses the `onRenderTab`
    function to override the default headers, where a custom header
    mapping is supplied.  Note: where possible, it is likely better to
    use the.

    `headers` is a dict with keys:

    - string (a list of or a singular dash component, string or number; required)

- model (boolean | number | string | dict | list; required):
    Model layout.

- popoutURL (string; default '/assets/popout.html'):
    URL of popout window relative to origin, defaults to popout.html.

- realtimeResize (boolean; optional):
    boolean value, defaults to False, resize tabs as splitters are
    dragged. Warning: this can cause resizing to become choppy when
    tabs are slow to draw.

- supportsPopout (boolean; optional):
    if left undefined will do simple check based on userAgent.

- useStateForModel (boolean; optional):
    Flag that we should use internal state to manage the layout. If
    the layout is not being used by dash anywhere (for example, saving
    and re-hydrating the layout), it is more efficient to use the
    internal state (as this limits the number of round trips between
    JSON and the Model object).  WARNING: If you set this, do not
    expect the dash property `model` to reflect the current state of
    the layout!."""
    _children_props = ['headers.string']
    _base_nodes = ['children']
    _namespace = 'dash_flexlayout'
    _type = 'FlexLayout'
    @_explicitize_args
    def __init__(self, children=None, font=Component.UNDEFINED, supportsPopout=Component.UNDEFINED, popoutURL=Component.UNDEFINED, realtimeResize=Component.UNDEFINED, model=Component.REQUIRED, headers=Component.UNDEFINED, useStateForModel=Component.UNDEFINED, debugMode=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'debugMode', 'font', 'headers', 'model', 'popoutURL', 'realtimeResize', 'supportsPopout', 'useStateForModel']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'debugMode', 'font', 'headers', 'model', 'popoutURL', 'realtimeResize', 'supportsPopout', 'useStateForModel']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['model']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        if 'children' not in _explicit_args:
            raise TypeError('Required argument children was not specified.')

        super(FlexLayout, self).__init__(children=children, **args)
