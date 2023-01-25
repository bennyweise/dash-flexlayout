import React from 'react';
import {DashComponentProps} from '../props';
import * as CaplinFlexLayout from "flexlayout-react";
import { IJsonModel } from 'flexlayout-react';

import 'flexlayout-react/style/light.css';

// import { IJsonModel } from 'flexlayout-react';

// type IJsonModel = {
//     global?: CaplinFlexLayout.;
//     borders?: CaplinFlexLayout.BorderNode[];
//     layout: CaplinFlexLayout.RowNode;
// }

type Props = {
    /**
     * Children
     */
    children: JSX.Element
} & DashComponentProps;

/**
 * Component description
 */
const Tab = (props: Props) => {
    const { id, children} = props;

    return (
        <React.Fragment>{children}</React.Fragment>
    )
}

Tab.defaultProps = {};

export default Tab;
