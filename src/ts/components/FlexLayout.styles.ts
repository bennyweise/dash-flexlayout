// MyComponent.styles.ts
import { createStyles, MantineNumberSize } from '@mantine/core';

// Styles params are optional
export interface MyComponentStylesParams {
  radius?: MantineNumberSize;
}

export default createStyles((theme, { radius }: MyComponentStylesParams) => ({
  // add all styles as usual
  root: { borderRadius: theme.fn.radius(radius) },
  title: { fontSize: theme.fontSizes.sm },
  description: { fontSize: theme.fontSizes.xs },
}));