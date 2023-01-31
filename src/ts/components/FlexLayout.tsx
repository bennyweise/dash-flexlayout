import React, { useState } from "react";
import { DashComponentProps } from "../props";
import * as CaplinFlexLayout from "flexlayout-react";
import { renderDashComponents, renderDashComponent } from "dash-extensions-js";

import { DefaultProps, Selectors, MantineNumberSize, Box } from "@mantine/core";
import useStyles, { MyComponentStylesParams } from "./FlexLayout.styles";

import "flexlayout-react/style/light.css";
import { TabSetNode } from "flexlayout-react";

// This type will contain a union with all selectors defined in useStyles,
// in this case it will be `'root' | 'title' | 'description'`
type FlexLayoutStylesNames = Selectors<typeof useStyles>;

type Props = {
  /**
   * the tab font (overrides value in css). Example: font={{size:"12px", style:"italic"}}
   */
  font?: any;

  /**
   * if left undefined will do simple check based on userAgent
   */
  supportsPopout?: boolean;

  /**
   * URL of popout window relative to origin, defaults to popout.html
   */
  popoutURL?: string;

  /**
   * boolean value, defaults to false, resize tabs as splitters are dragged. Warning: this can cause resizing to become choppy when tabs are slow to draw
   */
  realtimeResize?: boolean;

  /**
   * Model layout.
   */
  // Note that dash-generate-components fails to build when attempting to use IJsonModel here
  model: any;

  /**
   * List of children to be rendered. Children are allocated to their respective tab
   * based on the ID of the element.
   *
   * WARNING: There is no validation done on whether the children here will be rendered in any tab.
   * If there is no matching tab for a particular ID, that element will be silently ignored in
   * rendering (although callbacks will still be applied).
   */
  children: JSX.Element;

  /**
   * Map of headers to render for each tab. Uses the `onRenderTab` function to override
   * the default headers, where a custom header mapping is supplied.
   *
   * Note: where possible, it is likely better to use the
   */
  headers?: { string: JSX.Element };

  /**
   * Flag that we should use internal state to manage the layout. If the layout is not being
   * used by dash anywhere (for example, saving and re-hydrating the layout), it is more efficient
   * to use the internal state (as this limits the number of round trips between JSON
   * and the Model object).
   *
   * WARNING: If you set this, do not expect the dash property `model` to reflect the current
   * state of the layout!
   */
  useStateForModel?: boolean;

  /**
   *
   */
  debugMode?: boolean;
} & DashComponentProps;

const idMatches = (child: JSX.Element, id: string) => {
  return (
    ((child.props &&
      child.props._dashprivate_layout &&
      child.props._dashprivate_layout.props["id"]) ||
      (child.props && child.props["id"]) ||
      child.key) === id
  );
};

const getMatchingChildren = (
  children: JSX.Element,
  node: CaplinFlexLayout.TabNode
) => {
  const id = node.getId();
  const childArray = Array.isArray(children) ? children : [children];
  const matchedChildren = childArray.filter((child) => idMatches(child, id));
  return matchedChildren;
};

/**
 * Component description
 */
const FlexLayout = (props: Props) => {
  const {
    id,
    model,
    children,
    headers,
    setProps,
    useStateForModel,
    ...flProps
  } = props;
  const [modelState, setModelState] = useState(
    CaplinFlexLayout.Model.fromJson(model)
  );

  /**
   *
   */
  const getModel = () => {
    return setProps && !useStateForModel
      ? CaplinFlexLayout.Model.fromJson(model)
      : modelState;
  };

  /**
   * Whenever the model changes, if we are using dash to handle the layout,
   * we should call setProps to persist the updated layout. Otherwise
   * we do nothing and let the useState hook handle it.
   */
  const onModelChange = (model: CaplinFlexLayout.Model) => {
    setProps && !useStateForModel && setProps({ model: model.toJson() });
  };

  /**
   * Customise rendering of the tab to use the `headers` map
   * if available.
   */
  const onRenderTab = (
    node: CaplinFlexLayout.TabNode,
    renderValues: CaplinFlexLayout.ITabRenderValues
  ) => {
    if (headers && headers[node.getId()]) {
      const header = headers[node.getId()];
      renderValues.content =
        header.props && header.props._dashprivate_layout
          ? renderDashComponent(headers[node.getId()])
          : header;
    }
  };

  const factory = (node: CaplinFlexLayout.TabNode) => {
    const matchedChildren = getMatchingChildren(children, node);
    return <React.Fragment>{matchedChildren}</React.Fragment>;
  };
  return (
    <CaplinFlexLayout.Layout
      model={getModel()}
      factory={factory}
      onModelChange={onModelChange}
      onRenderTab={onRenderTab}
      {...flProps}
    />
  );
};

FlexLayout.defaultProps = {
  popoutURL: "/assets/popout.html",
};

export default FlexLayout;
