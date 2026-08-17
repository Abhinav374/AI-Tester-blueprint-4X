import { Page, Locator } from '@playwright/test';

export class LoginPage {
  private readonly page: Page;
  private readonly emailField: Locator;
  private readonly passwordField: Locator;
  private readonly signInButton: Locator;
  private readonly rememberMeCheckbox: Locator;
  private readonly rememberMeLabel: Locator;
  private readonly forgotPasswordButton: Locator;
  private readonly signInWithGoogle: Locator;
  private readonly signInUsingSSO: Locator;
  private readonly signInWithPasskey: Locator;
  private readonly errorMessage: Locator;
  private readonly dashboardHeading: Locator;

  constructor(page: Page) {
    this.page = page;
    this.emailField = page.getByPlaceholder('Enter email ID').first();
    this.passwordField = page.getByPlaceholder('Enter password').first();
    this.signInButton = page.getByRole('button', { name: 'Sign in' }).first();
    this.rememberMeCheckbox = page.locator('#checkbox-remember');
    this.rememberMeLabel = page.getByText('Remember me', { exact: true });
    this.forgotPasswordButton = page.getByRole('button', { name: 'Forgot Password?' });
    this.signInWithGoogle = page.getByText('Sign in with Google', { exact: true });
    this.signInUsingSSO = page.getByText('Sign in using SSO', { exact: true });
    this.signInWithPasskey = page.getByText('Sign in with Passkey', { exact: true });
    this.errorMessage = page.locator('#js-notification-box-msg');
    this.dashboardHeading = page.getByRole('heading', { name: /Dashboard/i });
  }

  async navigate(baseUrl: string): Promise<void> {
    try {
      await this.page.goto(baseUrl, { waitUntil: 'domcontentloaded' });
    } catch (error) {
      throw new Error(
        `Failed to navigate to ${baseUrl}. Current URL: ${this.getCurrentUrl()}. Cause: ${this.describe(error)}`
      );
    }
  }

  async enterEmail(email: string): Promise<void> {
    try {
      await this.emailField.fill(email);
    } catch (error) {
      throw new Error(
        `Failed to enter email. Email field was not interactable within the wait. Current URL: ${this.getCurrentUrl()}. Cause: ${this.describe(error)}`
      );
    }
  }

  async enterPassword(password: string): Promise<void> {
    try {
      await this.passwordField.fill(password);
    } catch (error) {
      throw new Error(
        `Failed to enter password. Password field was not interactable within the wait. Current URL: ${this.getCurrentUrl()}. Cause: ${this.describe(error)}`
      );
    }
  }

  async clickSignIn(): Promise<void> {
    try {
      await this.signInButton.click();
    } catch (error) {
      throw new Error(
        `Failed to click Sign in button. Sign in button was not clickable within the wait. Current URL: ${this.getCurrentUrl()}. Cause: ${this.describe(error)}`
      );
    }
  }

  async toggleRememberMe(): Promise<void> {
    try {
      await this.rememberMeLabel.click();
    } catch (error) {
      throw new Error(
        `Failed to toggle Remember me checkbox. Current URL: ${this.getCurrentUrl()}. Cause: ${this.describe(error)}`
      );
    }
  }

  async isRememberMeChecked(): Promise<boolean> {
    try {
      return await this.rememberMeCheckbox.isChecked();
    } catch (error) {
      throw new Error(
        `Failed to read Remember me checkbox state. Current URL: ${this.getCurrentUrl()}. Cause: ${this.describe(error)}`
      );
    }
  }

  async doLogin(email: string, password: string): Promise<void> {
    await this.enterEmail(email);
    await this.enterPassword(password);
    await this.clickSignIn();
  }

  async getErrorMessage(): Promise<string> {
    try {
      await this.errorMessage.waitFor({ state: 'visible', timeout: 10000 });
      return (await this.errorMessage.textContent())?.trim() ?? '';
    } catch {
      return '';
    }
  }

  async isDashboardVisible(): Promise<boolean> {
    try {
      await this.dashboardHeading.waitFor({ state: 'visible', timeout: 15000 });
      return true;
    } catch {
      return false;
    }
  }

  async isElementVisible(locator: Locator): Promise<boolean> {
    try {
      return await locator.isVisible();
    } catch {
      return false;
    }
  }

  getCurrentUrl(): string {
    try {
      return this.page.url();
    } catch {
      return '';
    }
  }

  private describe(error: unknown): string {
    return error instanceof Error ? error.message : String(error);
  }
}
