# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Tab(Component):
    """A Tab component.
This is a simple component that holds content to be rendered within a Tab.
Takes an ID that corresponds to a particular tab in the layout.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children to render within Tab.

- id (string; required):
    Unique ID to identify this component in Dash callbacks."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_flexlayout'
    _type = 'Tab'
    @_explicitize_args
    def __init__(self, children=None, id=Component.REQUIRED, **kwargs):
        self._prop_names = ['children', 'id']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Tab, self).__init__(children=children, **args)
