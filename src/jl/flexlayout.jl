# AUTO GENERATED FILE - DO NOT EDIT

export flexlayout

"""
    flexlayout(;kwargs...)
    flexlayout(children::Any;kwargs...)
    flexlayout(children_maker::Function;kwargs...)


A FlexLayout component.
Component description
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; required): List of children to be rendered. Children are allocated to their respective tab
based on the ID of the element.

WARNING: There is no validation done on whether the children here will be rendered in any tab.
If there is no matching tab for a particular ID, that element will be silently ignored in
rendering (although callbacks will still be applied).
- `id` (String; optional): Unique ID to identify this component in Dash callbacks.
- `debugMode` (Bool; optional)
- `font` (Bool | Real | String | Dict | Array; optional): the tab font (overrides value in css). Example: font={{size:"12px", style:"italic"}}
- `model` (Bool | Real | String | Dict | Array; required): Model layout.
- `popoutURL` (String; optional): URL of popout window relative to origin, defaults to popout.html
- `realtimeResize` (Bool; optional): boolean value, defaults to false, resize tabs as splitters are dragged. Warning: this can cause resizing to become choppy when tabs are slow to draw
- `supportsPopout` (Bool; optional): if left undefined will do simple check based on userAgent
- `useStateForModel` (Bool; optional): Flag that we should use internal state to manage the layout. If the layout is not being
used by dash anywhere (for example, saving and re-hydrating the layout), it is more efficient
to use the internal state (as this limits the number of round trips between JSON
and the Model object).

WARNING: If you set this, do not expect the dash property `model` to reflect the current
state of the layout!
"""
function flexlayout(; kwargs...)
        available_props = Symbol[:children, :id, :debugMode, :font, :model, :popoutURL, :realtimeResize, :supportsPopout, :useStateForModel]
        wild_props = Symbol[]
        return Component("flexlayout", "FlexLayout", "dash_flexlayout", available_props, wild_props; kwargs...)
end

flexlayout(children::Any; kwargs...) = flexlayout(;kwargs..., children = children)
flexlayout(children_maker::Function; kwargs...) = flexlayout(children_maker(); kwargs...)

