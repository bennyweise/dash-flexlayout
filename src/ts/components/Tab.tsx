import React from "react";
import { DashComponentProps } from "../props";
import * as CaplinFlexLayout from "flexlayout-react";
import { IJsonModel } from "flexlayout-react";

type Props = {
  /**
   * Unique ID to identify this component in Dash callbacks.
   */
  id: string;

  /**
   * Children to render within Tab
   */
  children?: React.ReactNode;
};

/**
 * This is a simple component that holds content to be rendered within a Tab.
 * Takes an ID that corresponds to a particular tab in the layout.
 */
const Tab = (props: Props) => {
  const { id, children } = props;

  return <React.Fragment>{children}</React.Fragment>;
};

Tab.defaultProps = {};

export default Tab;
