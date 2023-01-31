# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MantineProvider(Component):
    """A MantineProvider component.
Mantine Provider

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- inherit (boolean; optional):
    Inherit from one level up MantineProvider.

- theme (dict; optional):
    Theme.

- withCSSVariables (boolean; optional):
    With css variables.

- withGlobalStyles (boolean; optional):
    With global styles.

- withNormalizeCSS (boolean; optional):
    Normalize CSS."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_flexlayout'
    _type = 'MantineProvider'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, theme=Component.UNDEFINED, withNormalizeCSS=Component.UNDEFINED, withGlobalStyles=Component.UNDEFINED, withCSSVariables=Component.UNDEFINED, inherit=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'inherit', 'theme', 'withCSSVariables', 'withGlobalStyles', 'withNormalizeCSS']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'inherit', 'theme', 'withCSSVariables', 'withGlobalStyles', 'withNormalizeCSS']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MantineProvider, self).__init__(children=children, **args)
