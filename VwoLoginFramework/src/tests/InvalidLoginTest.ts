import { test, expect } from './fixtures';

const INVALID_CREDENTIALS_ERROR = 'Your email, password, IP address or location did not match';

const invalidCases: Array<{ email: string; password: string }> = [
  { email: '', password: '' },
  { email: 'invalid-email', password: '' },
  { email: 'invalid@example.com', password: 'wrongpassword123' },
  { email: 'wronguser@example.com', password: 'wrongpassword' },
];

for (const { email, password } of invalidCases) {
  test(`invalid login rejects with ${email || '(empty)'}/${password || '(empty)'}`, async ({ loginPage }) => {
    await loginPage.doLogin(email, password);
    const actualError = await loginPage.getErrorMessage();
    expect(actualError, `Expected '${INVALID_CREDENTIALS_ERROR}' but got '${actualError}' at URL ${loginPage.getCurrentUrl()}`).toBe(
      INVALID_CREDENTIALS_ERROR
    );
  });
}

test('remember me checkbox toggles', async ({ loginPage }) => {
  await loginPage.toggleRememberMe();
  expect(await loginPage.isRememberMeChecked(), 'Remember me should be checked after toggle').toBe(true);
  await loginPage.toggleRememberMe();
  expect(await loginPage.isRememberMeChecked(), 'Remember me should be unchecked after second toggle').toBe(false);
});
