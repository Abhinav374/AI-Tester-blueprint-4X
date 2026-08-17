import { test, expect } from './fixtures';
import { readConfig } from '../config/config';

const config = readConfig();
const hasCredentials = Boolean(config.email && config.password);

test('valid login with external credentials', async ({ loginPage }) => {
  test.skip(!hasCredentials, 'VWO_EMAIL and VWO_PASSWORD must be set to run the valid login test');
  await loginPage.doLogin(config.email, config.password);
  const dashboardVisible = await loginPage.isDashboardVisible();
  expect(dashboardVisible, `Login did not reach the dashboard. Current URL: ${loginPage.getCurrentUrl()}`).toBe(true);
});
