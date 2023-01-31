# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MyComponent(Component):
    """A MyComponent component.
Test component for theming

Keyword arguments:
"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_flexlayout'
    _type = 'MyComponent'
    @_explicitize_args
    def __init__(self, **kwargs):
        self._prop_names = []
        self._valid_wildcard_attributes =            []
        self.available_properties = []
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MyComponent, self).__init__(**args)
