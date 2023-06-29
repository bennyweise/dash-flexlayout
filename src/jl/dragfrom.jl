# AUTO GENERATED FILE - DO NOT EDIT

export dragfrom

"""
    dragfrom(;kwargs...)
    dragfrom(children::Any;kwargs...)
    dragfrom(children_maker::Function;kwargs...)


A DragFrom component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional)
- `id` (String; optional): Unique ID to identify this component in Dash callbacks.
- `effectAllowed` (String; optional)
- `name` (String; optional)
- `transferType` (String; optional)
"""
function dragfrom(; kwargs...)
        available_props = Symbol[:children, :id, :effectAllowed, :name, :transferType]
        wild_props = Symbol[]
        return Component("dragfrom", "DragFrom", "dash_flexlayout", available_props, wild_props; kwargs...)
end

dragfrom(children::Any; kwargs...) = dragfrom(;kwargs..., children = children)
dragfrom(children_maker::Function; kwargs...) = dragfrom(children_maker(); kwargs...)

