import React from 'react';
import {DashComponentProps} from '../props';

type Props = {
    // Insert props
} & DashComponentProps;

/**
 * Component description
 */
const FlexLayout = (props: Props) => {
    const { id } = props;
    return (
        <div id={id}>
            {"This is a FlexLayout component"}
        </div>
    )
}

FlexLayout.defaultProps = {};

export default FlexLayout;
