// MyComponent.tsx
import React from "react";
import {
  DefaultProps,
  Selectors,
  MantineNumberSize,
  Box,
  useMantineColorScheme,
  useMantineTheme,
  Title,
} from "@mantine/core";
import useStyles, { MyComponentStylesParams } from "./MyComponent.styles";

// This type will contain a union with all selectors defined in useStyles,
// in this case it will be `'root' | 'title' | 'description'`
type MyComponentStylesNames = Selectors<typeof useStyles>;

// DefaultProps adds system props support (margin, padding, sx, unstyled, styles and classNames).
// It accepts 2 types: styles names and styles params, both of them are optional
interface MyComponentProps
  extends DefaultProps<MyComponentStylesNames, MyComponentStylesParams> {
  radius?: MantineNumberSize;
}

/**
 * Test component for theming
 */
const MyComponent = (props: any) => {
  const { classNames, styles, unstyled, radius, className, ...others } = props;
  //   const { classes, cx, theme } = useStyles(
  //     // First argument of useStyles is styles params
  //     { radius },
  //     // Second argument is responsible for styles api integration
  //     { name: "MyComponent", classNames, styles, unstyled }
  //   );
  const theme = useMantineTheme();
  console.log(theme);
  //   const colorScheme = useMantineColorScheme();
  //   console.log(colorScheme);
  //   console.log(theme);

  return (
    <Box {...others}>
      <Title className={theme.colorScheme}>
        {"Awesome component - " + theme.colorScheme}
      </Title>
      <div className={""}>With Styles API support</div>
    </Box>
  );
};

export default MyComponent;
