# AUTO GENERATED FILE - DO NOT EDIT

export flexlayout

"""
    flexlayout(;kwargs...)
    flexlayout(children::Any;kwargs...)
    flexlayout(children_maker::Function;kwargs...)


A FlexLayout component.
Component description
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; required): Layout nodes
- `id` (String; optional): Unique ID to identify this component in Dash callbacks.
- `config` (Bool | Real | String | Dict | Array; required): Layout config
"""
function flexlayout(; kwargs...)
        available_props = Symbol[:children, :id, :config]
        wild_props = Symbol[]
        return Component("flexlayout", "FlexLayout", "dash_flexlayout", available_props, wild_props; kwargs...)
end

flexlayout(children::Any; kwargs...) = flexlayout(;kwargs..., children = children)
flexlayout(children_maker::Function; kwargs...) = flexlayout(children_maker(); kwargs...)

