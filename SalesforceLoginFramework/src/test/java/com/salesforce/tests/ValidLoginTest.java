package com.salesforce.tests;

import com.salesforce.framework.base.BaseTest;
import com.salesforce.framework.config.ConfigReader;
import com.salesforce.framework.pages.LoginPage;
import org.openqa.selenium.WebDriverException;
import org.testng.Assert;
import org.testng.annotations.Test;

public class ValidLoginTest extends BaseTest {

    @Test
    public void testValidLogin() {
        ConfigReader configReader = ConfigReader.getInstance();
        String username = configReader.getUsername();
        String password = configReader.getPassword();

        Assert.assertFalse(username.isEmpty(), "Username must be configured in config.properties for the valid login test.");
        Assert.assertFalse(password.isEmpty(), "Password must be configured in config.properties for the valid login test.");

        LoginPage loginPage = new LoginPage(driver, configReader.getExplicitWait());

        try {
            loginPage.doLogin(username, password);
            Assert.assertTrue(loginPage.isLoggedIn(configReader.getHomePageVerifier()),
                    "Login did not reach the authenticated home page. Current URL: " + loginPage.getCurrentUrl());
            Assert.assertTrue(loginPage.getCurrentUrl().contains("my.salesforce.com")
                            || loginPage.getCurrentUrl().contains("lightning.force.com")
                            || loginPage.getCurrentUrl().contains("salesforce.com"),
                    "Post-login URL is not a Salesforce domain. Current URL: " + loginPage.getCurrentUrl());
        } catch (WebDriverException e) {
            Assert.fail("Valid login failed with exception: " + e.getMessage()
                    + " | Page state URL: " + loginPage.getCurrentUrl()
                    + " | Error text: " + loginPage.getErrorMessage());
        }
    }
}
