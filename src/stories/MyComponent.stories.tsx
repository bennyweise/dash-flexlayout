import React from "react";
import { ComponentStory, ComponentMeta } from "@storybook/react";

import { MyComponent } from "../ts/index";
import { MantineProvider } from "@mantine/core";

export default {
  title: "Layout/MyComponent",
  component: MyComponent,
  // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
  argTypes: {
    backgroundColor: { control: "color" },
  },
} as ComponentMeta<typeof MyComponent>;

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
const Template: ComponentStory<typeof MyComponent> = ({ label, theme }) => (
  <MantineProvider theme={theme}>
    <MyComponent label={label} />
  </MantineProvider>
);

export const Primary = Template.bind({});
// More on args: https://storybook.js.org/docs/react/writing-stories/args
Primary.args = {
  label: "MyComponent",
  theme: { colorScheme: "light" },
};

export const Dark = Template.bind({});
// More on args: https://storybook.js.org/docs/react/writing-stories/args
Dark.args = {
  label: "MyComponent",
  theme: { colorScheme: "dark" },
};
