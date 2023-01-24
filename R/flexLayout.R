# AUTO GENERATED FILE - DO NOT EDIT

#' @export
flexLayout <- function(id=NULL) {
    
    props <- list(id=id)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FlexLayout',
        namespace = 'dash_flexlayout',
        propNames = c('id'),
        package = 'dashFlexlayout'
        )

    structure(component, class = c('dash_component', 'list'))
}
