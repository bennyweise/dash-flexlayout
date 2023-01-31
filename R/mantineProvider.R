# AUTO GENERATED FILE - DO NOT EDIT

#' @export
mantineProvider <- function(children=NULL, id=NULL, inherit=NULL, theme=NULL, withCSSVariables=NULL, withGlobalStyles=NULL, withNormalizeCSS=NULL) {
    
    props <- list(children=children, id=id, inherit=inherit, theme=theme, withCSSVariables=withCSSVariables, withGlobalStyles=withGlobalStyles, withNormalizeCSS=withNormalizeCSS)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'MantineProvider',
        namespace = 'dash_flexlayout',
        propNames = c('children', 'id', 'inherit', 'theme', 'withCSSVariables', 'withGlobalStyles', 'withNormalizeCSS'),
        package = 'dashFlexlayout'
        )

    structure(component, class = c('dash_component', 'list'))
}
