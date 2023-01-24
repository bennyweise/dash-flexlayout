import React from 'react';
import {DashComponentProps} from '../props';
import * as CaplinFlexLayout from "flexlayout-react";
import { IJsonModel } from 'flexlayout-react';

type Props = {
    /**
     * Layout config
     */
    config: CaplinFlexLayout.IJsonModel,

    /**
     * Layout nodes
     */
    nodes: {string: React.ReactChild }
} & DashComponentProps;

/**
 * Component description
 */
const FlexLayout = (props: Props) => {
    const { id, config, nodes } = props;
    const modelConfig = CaplinFlexLayout.Model.fromJson(config);

    const factory = (node: CaplinFlexLayout.TabNode) => {
        console.log(node);
        console.log(node.getChildren());
        console.log(node.getComponent());
        // return <div>{"This is a node"}</div>
        return <div>{nodes[node.getId()]}</div>
    }
    return (
        <CaplinFlexLayout.Layout model={modelConfig} factory={factory}/>
    )
}

FlexLayout.defaultProps = {};

export default FlexLayout;
