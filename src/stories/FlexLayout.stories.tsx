import React from "react";
import { ComponentStory, ComponentMeta } from "@storybook/react";

import { FlexLayout, Tab } from "../ts/index";

// import "flexlayout-react/style/light.css";

var json = {
  global: { tabEnableClose: false, tabEnableFloat: true },
  borders: [
    {
      type: "border",
      location: "bottom",
      size: 100,
      children: [
        {
          type: "tab",
          name: "four",
          component: "text",
        },
      ],
    },
    {
      type: "border",
      location: "left",
      size: 100,
      children: [],
    },
  ],
  layout: {
    type: "row",
    weight: 100,
    children: [
      {
        type: "tabset",
        weight: 50,
        selected: 0,
        children: [
          {
            type: "tab",
            name: "One",
            component: "text",
            enableFloat: true,
            id: "tab-1",
          },
        ],
      },
      {
        type: "tabset",
        weight: 50,
        selected: 0,
        children: [
          {
            type: "tab",
            name: "Two",
            component: "text",
            id: "tab-2",
          },
          {
            type: "tab",
            name: "Three",
            component: "text",
            id: "tab-3",
          },
        ],
      },
    ],
  },
};

export default {
  title: "Layout/FlexLayout",
  component: FlexLayout,
  // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
  argTypes: {
    backgroundColor: { control: "color" },
  },
} as ComponentMeta<typeof FlexLayout>;

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
const Template: ComponentStory<typeof FlexLayout> = (args) => (
  <FlexLayout {...args} />
);

export const Primary = Template.bind({});
// More on args: https://storybook.js.org/docs/react/writing-stories/args
Primary.args = {
  primary: true,
  label: "FlexLayout",
  model: json,
  children: [
    <Tab id={"tab-1"}>{"something here"}</Tab>,
    <Tab id={"tab-2"}>{"something here in tab 2"}</Tab>,
    <Tab id={"tab-3"}>{"something here in tab 3"}</Tab>,
  ],
};

export const CustomTabHeader = Template.bind({});
// More on args: https://storybook.js.org/docs/react/writing-stories/args
CustomTabHeader.args = {
  primary: false,
  label: "Custom Header",
  model: json,
  children: [
    <Tab id={"tab-1"}>{"something here"}</Tab>,
    <Tab id={"tab-2"}>{"something here in tab 2"}</Tab>,
    <Tab id={"tab-3"}>{"something here in tab 3"}</Tab>,
  ],
  headers: {
    "tab-1": <h4>{"This is a custom tab 2 header"}</h4>,
    "tab-2": <h4>{"This is a custom tab 2 header"}</h4>,
    "tab-3": <h4>{"This is a custom tab 2 header"}</h4>,
  },
};
