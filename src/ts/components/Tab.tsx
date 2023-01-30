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

  /**
   * Has rendered prop
   */
  rendered?: boolean;
} & DashComponentProps;

/**
 * This is a simple component that holds content to be rendered within a Tab.
 * Takes an ID that corresponds to a particular tab in the layout.
 */
const Tab = (props: Props) => {
  const { id, children, setProps } = props;
  // Updates on first rendering
  //   setProps && setProps({ rendered: true });
  return <React.Fragment>{children}</React.Fragment>;
};

Tab.defaultProps = {};

const areEqual = (prevProps, nextProps) => {
  console.log("Checking for Tab re-render");
  console.log(prevProps);
  if (prevProps.heading === nextProps.heading) {
    return true; // donot re-render
  }
  return true; // will re-render
};

export default React.memo(Tab, areEqual);
