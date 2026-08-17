| Element              | Recommended Playwright locator                           | Locator type | Stability |
| -------------------- | -------------------------------------------------------- | ------------ | --------- |
| Email                | `page.getByPlaceholder('Enter email ID')`                | Placeholder  | ★★★★★     |
| Password             | `page.getByPlaceholder('Enter password')`                | Placeholder  | ★★★★★     |
| Sign In              | `page.getByRole('button', { name: 'Sign in' })`          | ARIA Role    | ★★★★★     |
| Remember Me          | `page.getByLabel('Remember me')`                         | Label        | ★★★★★     |
| Forgot Password      | `page.getByRole('button', { name: 'Forgot Password?' })` | ARIA Role    | ★★★★★     |
| Sign in with Google  | `page.getByText('Sign in with Google')`                  | Text         | ★★★★☆     |
| Sign in using SSO    | `page.getByText('Sign in using SSO')`                    | Text         | ★★★★☆     |
| Sign in with Passkey | `page.getByText('Sign in with Passkey')`                 | Text         | ★★★★☆     |
| Start Free Trial     | `page.getByText('Start a free trial')`                   | Text         | ★★★★☆     |
