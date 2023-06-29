# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dragFrom <- function(children=NULL, id=NULL, effectAllowed=NULL, name=NULL, transferType=NULL) {
    
    props <- list(children=children, id=id, effectAllowed=effectAllowed, name=name, transferType=transferType)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DragFrom',
        namespace = 'dash_flexlayout',
        propNames = c('children', 'id', 'effectAllowed', 'name', 'transferType'),
        package = 'dashFlexlayout'
        )

    structure(component, class = c('dash_component', 'list'))
}
