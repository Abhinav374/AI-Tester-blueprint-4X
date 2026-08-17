package com.salesforce.tests;

import com.salesforce.framework.base.BaseTest;
import com.salesforce.framework.config.ConfigReader;
import com.salesforce.framework.pages.LoginPage;
import org.openqa.selenium.WebDriverException;
import org.testng.Assert;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

public class InvalidLoginTest extends BaseTest {

    @DataProvider(name = "invalidCredentials")
    public Object[][] invalidCredentials() {
        ConfigReader configReader = ConfigReader.getInstance();
        String validUsername = configReader.getUsername();
        return new Object[][]{
                {"", "", "Please enter your username."},
                {validUsername, "", "Please enter your password."},
                {"invalid@example.com", "invalidpassword123", "Please check your username and password. If you still can't log in, contact your Salesforce administrator."},
                {"wronguser@example.com", "wrongpassword", "Please check your username and password. If you still can't log in, contact your Salesforce administrator."}
        };
    }

    @Test(dataProvider = "invalidCredentials")
    public void testInvalidLogin(String username, String password, String expectedError) {
        LoginPage loginPage = new LoginPage(driver, ConfigReader.getInstance().getExplicitWait());

        try {
            loginPage.clearUsernameField();
            loginPage.clearPasswordField();
            loginPage.doLogin(username, password);
            Assert.assertTrue(loginPage.isErrorDisplayed(), "Error message was not displayed for invalid login attempt.");
            Assert.assertEquals(loginPage.getErrorMessage(), expectedError,
                    "Error message text does not match expected value. Actual: " + loginPage.getErrorMessage());
        } catch (WebDriverException e) {
            Assert.fail("Invalid login test failed with exception: " + e.getMessage()
                    + " | Page state URL: " + loginPage.getCurrentUrl()
                    + " | Error text: " + loginPage.getErrorMessage());
        }
    }

    @Test
    public void testRememberMeCheckboxToggle() {
        LoginPage loginPage = new LoginPage(driver, ConfigReader.getInstance().getExplicitWait());

        try {
            loginPage.clickRememberMe();
            Assert.assertTrue(loginPage.isRememberMeSelected(), "Remember me checkbox should be selected after click.");
            loginPage.clickRememberMe();
            Assert.assertFalse(loginPage.isRememberMeSelected(), "Remember me checkbox should be deselected after second click.");
        } catch (WebDriverException e) {
            Assert.fail("Remember me checkbox toggle test failed with exception: " + e.getMessage()
                    + " | Page state URL: " + loginPage.getCurrentUrl());
        }
    }
}
