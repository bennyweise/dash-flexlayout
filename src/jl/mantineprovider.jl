# AUTO GENERATED FILE - DO NOT EDIT

export mantineprovider

"""
    mantineprovider(;kwargs...)
    mantineprovider(children::Any;kwargs...)
    mantineprovider(children_maker::Function;kwargs...)


A MantineProvider component.
Mantine Provider
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): Children
- `id` (String; optional): Unique ID to identify this component in Dash callbacks.
- `inherit` (Bool; optional): Inherit from one level up MantineProvider
- `theme` (Dict; optional): Theme
- `withCSSVariables` (Bool; optional): With css variables
- `withGlobalStyles` (Bool; optional): With global styles
- `withNormalizeCSS` (Bool; optional): Normalize CSS
"""
function mantineprovider(; kwargs...)
        available_props = Symbol[:children, :id, :inherit, :theme, :withCSSVariables, :withGlobalStyles, :withNormalizeCSS]
        wild_props = Symbol[]
        return Component("mantineprovider", "MantineProvider", "dash_flexlayout", available_props, wild_props; kwargs...)
end

mantineprovider(children::Any; kwargs...) = mantineprovider(;kwargs..., children = children)
mantineprovider(children_maker::Function; kwargs...) = mantineprovider(children_maker(); kwargs...)

