package com.salesforce.framework.pages;

import com.salesforce.framework.config.ConfigReader;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class LoginPage {

    @FindBy(xpath = "//input[@id='username']")
    private WebElement usernameField;

    @FindBy(xpath = "//input[@id='password']")
    private WebElement passwordField;

    @FindBy(xpath = "//input[@id='Login']")
    private WebElement loginButton;

    @FindBy(xpath = "//input[@id='rememberUn']")
    private WebElement rememberMeCheckbox;

    @FindBy(xpath = "//div[@id='error']")
    private WebElement errorContainer;

    private final WebDriver driver;
    private final WebDriverWait wait;

    public LoginPage(WebDriver driver, int explicitWaitSeconds) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(explicitWaitSeconds));
        PageFactory.initElements(driver, this);
    }

    public void enterUsername(String username) {
        try {
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    org.openqa.selenium.By.xpath("//input[@id='username']"))).sendKeys(username);
        } catch (TimeoutException e) {
            throw new org.openqa.selenium.WebDriverException(
                    "Failed to enter username. Username field was not visible within the explicit wait.", e);
        }
    }

    public void enterPassword(String password) {
        try {
            wait.until(ExpectedConditions.presenceOfElementLocated(
                    org.openqa.selenium.By.xpath("//input[@id='password']"))).sendKeys(password);
        } catch (TimeoutException e) {
            throw new org.openqa.selenium.WebDriverException(
                    "Failed to enter password. Password field was not present within the explicit wait.", e);
        }
    }

    public void clickLogin() {
        try {
            wait.until(ExpectedConditions.elementToBeClickable(
                    org.openqa.selenium.By.xpath("//input[@id='Login']"))).click();
        } catch (TimeoutException e) {
            throw new org.openqa.selenium.WebDriverException(
                    "Failed to click Login button. Login button was not clickable within the explicit wait.", e);
        }
    }

    public void clickRememberMe() {
        try {
            wait.until(ExpectedConditions.elementToBeClickable(
                    org.openqa.selenium.By.xpath("//input[@id='rememberUn']"))).click();
        } catch (TimeoutException e) {
            throw new org.openqa.selenium.WebDriverException(
                    "Failed to click Remember me checkbox. Checkbox was not clickable within the explicit wait.", e);
        }
    }

    public boolean isRememberMeSelected() {
        try {
            return wait.until(ExpectedConditions.elementToBeClickable(
                    org.openqa.selenium.By.xpath("//input[@id='rememberUn']"))).isSelected();
        } catch (TimeoutException e) {
            throw new org.openqa.selenium.WebDriverException(
                    "Failed to read Remember me checkbox state.", e);
        }
    }

    public void doLogin(String username, String password) {
        enterUsername(username);
        enterPassword(password);
        clickLogin();
    }

    public boolean isErrorDisplayed() {
        try {
            return wait.until(ExpectedConditions.visibilityOfElementLocated(
                    org.openqa.selenium.By.xpath("//div[@id='error']"))).isDisplayed();
        } catch (TimeoutException e) {
            return false;
        }
    }

    public String getErrorMessage() {
        try {
            return wait.until(ExpectedConditions.visibilityOfElementLocated(
                    org.openqa.selenium.By.xpath("//div[@id='error']"))).getText().trim();
        } catch (TimeoutException e) {
            return "";
        }
    }

    public boolean isLoggedIn(String homePageVerifierXpath) {
        try {
            return wait.until(ExpectedConditions.visibilityOfElementLocated(
                    org.openqa.selenium.By.xpath(homePageVerifierXpath))).isDisplayed();
        } catch (TimeoutException e) {
            return false;
        }
    }

    public String getCurrentUrl() {
        try {
            return driver.getCurrentUrl();
        } catch (org.openqa.selenium.WebDriverException e) {
            return "";
        }
    }

    public void clearUsernameField() {
        try {
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                    org.openqa.selenium.By.xpath("//input[@id='username']"))).clear();
        } catch (TimeoutException e) {
            throw new org.openqa.selenium.WebDriverException(
                    "Failed to clear username field.", e);
        }
    }

    public void clearPasswordField() {
        try {
            wait.until(ExpectedConditions.presenceOfElementLocated(
                    org.openqa.selenium.By.xpath("//input[@id='password']"))).clear();
        } catch (TimeoutException e) {
            throw new org.openqa.selenium.WebDriverException(
                    "Failed to clear password field. Password field was not present within the explicit wait.", e);
        }
    }

    private WebElement username() {
        return usernameField;
    }

    private WebElement password() {
        return passwordField;
    }

    private WebElement loginButtonElement() {
        return loginButton;
    }

    private WebElement rememberMeCheckboxElement() {
        return rememberMeCheckbox;
    }

    private WebElement errorContainerElement() {
        return errorContainer;
    }
}
