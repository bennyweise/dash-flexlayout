# AUTO GENERATED FILE - DO NOT EDIT

#' @export
flexLayout <- function(children=NULL, id=NULL, debugMode=NULL, font=NULL, headers=NULL, model=NULL, popoutURL=NULL, realtimeResize=NULL, supportsPopout=NULL, useStateForModel=NULL) {
    
    props <- list(children=children, id=id, debugMode=debugMode, font=font, headers=headers, model=model, popoutURL=popoutURL, realtimeResize=realtimeResize, supportsPopout=supportsPopout, useStateForModel=useStateForModel)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FlexLayout',
        namespace = 'dash_flexlayout',
        propNames = c('children', 'id', 'debugMode', 'font', 'headers', 'model', 'popoutURL', 'realtimeResize', 'supportsPopout', 'useStateForModel'),
        package = 'dashFlexlayout'
        )

    structure(component, class = c('dash_component', 'list'))
}
