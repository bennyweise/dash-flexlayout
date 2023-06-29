# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DragFrom(Component):
    """A DragFrom component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- effectAllowed (string; optional)

- name (string; optional)

- transferType (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_flexlayout'
    _type = 'DragFrom'
    @_explicitize_args
    def __init__(self, children=None, effectAllowed=Component.UNDEFINED, transferType=Component.UNDEFINED, name=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'effectAllowed', 'name', 'transferType']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'effectAllowed', 'name', 'transferType']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DragFrom, self).__init__(children=children, **args)
