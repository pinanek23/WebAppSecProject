import type { CSSObject, MantineTheme } from '@mantine/core'

const globalStyles = (theme: MantineTheme): Record<string, CSSObject> => ({
  body: {
    backgroundColor: theme.colorScheme === 'dark' ? '#1d1d1d' : '#eff4f6',
    color: theme.colorScheme === 'dark' ? '#f1f1f1' : '#1d1d1d',
    lineHeight: theme.lineHeight
  }
})

export { globalStyles }
