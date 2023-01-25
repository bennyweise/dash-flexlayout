# AUTO GENERATED FILE - DO NOT EDIT

export tab

"""
    tab(;kwargs...)
    tab(children::Any;kwargs...)
    tab(children_maker::Function;kwargs...)


A Tab component.
Component description
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; required): Children
- `id` (String; optional): Unique ID to identify this component in Dash callbacks.
"""
function tab(; kwargs...)
        available_props = Symbol[:children, :id]
        wild_props = Symbol[]
        return Component("tab", "Tab", "dash_flexlayout", available_props, wild_props; kwargs...)
end

tab(children::Any; kwargs...) = tab(;kwargs..., children = children)
tab(children_maker::Function; kwargs...) = tab(children_maker(); kwargs...)

