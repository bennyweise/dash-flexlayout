% Auto-generated: do not edit by hand
\name{flexLayout}

\alias{flexLayout}

\title{FlexLayout component}

\description{
Component description
}

\usage{
flexLayout(children=NULL, id=NULL, debugMode=NULL, font=NULL,
headers=NULL, model=NULL, popoutURL=NULL,
realtimeResize=NULL, supportsPopout=NULL,
useStateForModel=NULL)
}

\arguments{
\item{children}{A list of or a singular dash component, string or number. List of children to be rendered. Children are allocated to their respective tab
based on the ID of the element.

WARNING: There is no validation done on whether the children here will be rendered in any tab.
If there is no matching tab for a particular ID, that element will be silently ignored in
rendering (although callbacks will still be applied).}

\item{id}{Character. Unique ID to identify this component in Dash callbacks.}

\item{debugMode}{Logical. }

\item{font}{Logical | numeric | character | named list | unnamed list. the tab font (overrides value in css). Example: font={{size:"12px", style:"italic"}}}

\item{headers}{Lists containing elements 'string'.
those elements have the following types:
  - string (a list of or a singular dash component, string or number; required). Map of headers to render for each tab. Uses the `onRenderTab` function to override
the default headers, where a custom header mapping is supplied.

Note: where possible, it is likely better to use the}

\item{model}{Logical | numeric | character | named list | unnamed list. Model layout.}

\item{popoutURL}{Character. URL of popout window relative to origin, defaults to popout.html}

\item{realtimeResize}{Logical. boolean value, defaults to false, resize tabs as splitters are dragged. Warning: this can cause resizing to become choppy when tabs are slow to draw}

\item{supportsPopout}{Logical. if left undefined will do simple check based on userAgent}

\item{useStateForModel}{Logical. Flag that we should use internal state to manage the layout. If the layout is not being
used by dash anywhere (for example, saving and re-hydrating the layout), it is more efficient
to use the internal state (as this limits the number of round trips between JSON
and the Model object).

WARNING: If you set this, do not expect the dash property `model` to reflect the current
state of the layout!}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

