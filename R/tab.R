# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tab <- function(children=NULL, id=NULL) {
    
    props <- list(children=children, id=id)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Tab',
        namespace = 'dash_flexlayout',
        propNames = c('children', 'id'),
        package = 'dashFlexlayout'
        )

    structure(component, class = c('dash_component', 'list'))
}
