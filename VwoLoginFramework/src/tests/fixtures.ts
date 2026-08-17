import { test as base } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';
import { readConfig } from '../config/config';

type Fixtures = {
  loginPage: LoginPage;
};

export const test = base.extend<Fixtures>({
  loginPage: async ({ page }, use) => {
    const config = readConfig();
    const loginPage = new LoginPage(page);
    await loginPage.navigate(config.baseUrl);
    await use(loginPage);
  },
});

export { expect } from '@playwright/test';
