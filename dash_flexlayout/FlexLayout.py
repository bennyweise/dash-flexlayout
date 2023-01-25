# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FlexLayout(Component):
    """A FlexLayout component.
Component description

Keyword arguments:

- children (a list of or a singular dash component, string or number; required):
    Layout nodes.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- config (boolean | number | string | dict | list; required):
    Layout config."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_flexlayout'
    _type = 'FlexLayout'
    @_explicitize_args
    def __init__(self, children=None, config=Component.REQUIRED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'config']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'config']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['config']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        if 'children' not in _explicit_args:
            raise TypeError('Required argument children was not specified.')

        super(FlexLayout, self).__init__(children=children, **args)
