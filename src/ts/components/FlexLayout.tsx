import React, {useState} from 'react';
import {DashComponentProps} from '../props';
import * as CaplinFlexLayout from "flexlayout-react";
import { IJsonModel } from 'flexlayout-react';
import { renderDashComponents } from "dash-extensions-js";

import 'flexlayout-react/style/light.css';

// import { IJsonModel } from 'flexlayout-react';

// type IJsonModel = {
//     global?: CaplinFlexLayout.;
//     borders?: CaplinFlexLayout.BorderNode[];
//     layout: CaplinFlexLayout.RowNode;
// }

type Props = {
    /**
     * Layout config
     */
    // Note that dash-generate-components fails to build when attempting to use IJsonModel here
    config: any,

    /**
     * Layout nodes
     */
    children: JSX.Element
} & DashComponentProps;


const getChildElement = (children: JSX.Element, node: CaplinFlexLayout.TabNode) => {
    if (children.props && children.props._dashprivate_layout) {
        console.log("Retrieving from dash component");
        return children.props._dashprivate_layout[node.getId()];
    }
    return children[node.getId()];
}


const idMatches = (child: JSX.Element, id: string) => {
    return (
        (child.props &&
            child.props._dashprivate_layout &&
            child.props._dashprivate_layout.props['id']) ||
        (child.props && child.props['id']) ||
        child.key
    ) === id;
}

const getMatchingChildren = (children: JSX.Element, node: CaplinFlexLayout.TabNode) => {
    const id = node.getId();
    const childArray = Array.isArray(children) ? children : [children];
    const matchedChildren = childArray.filter(
        (child) => idMatches(child, id)
    );
    console.log("Found " + matchedChildren.length + " matching children for " + id);
    return matchedChildren;
}

/**
 * Component description
 */
const FlexLayout = (props: Props) => {
    const { id, config, children, setProps } = props;
    const [modelState, setModelState] = useState(
        CaplinFlexLayout.Model.fromJson(config)
    );
    console.log(children);

    const factory = (node: CaplinFlexLayout.TabNode) => {
        console.log(node);
        console.log(node.getChildren());
        console.log(node.getComponent());
        // return <div>{"This is a node"}</div>
        const matchedChildren = getMatchingChildren(children, node);
        return <React.Fragment>{matchedChildren}</React.Fragment>
    }
    return (
        <CaplinFlexLayout.Layout model={modelState} factory={factory}/>
    )
}

FlexLayout.defaultProps = {};

export default FlexLayout;
