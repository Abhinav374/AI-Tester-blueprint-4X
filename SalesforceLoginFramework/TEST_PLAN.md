# Test Plan — Salesforce Login Automation Framework

## 1. Scope

Automate and verify the Salesforce login page at `https://login.salesforce.com/?locale=in` using an enterprise-grade Selenium + Java + Maven + TestNG framework. Covers valid login, invalid login matrix, and Remember me checkbox UI behavior.

## 2. Framework Stack

| Component | Choice |
|-----------|--------|
| Language | Java 17 |
| Build | Maven |
| Test runner | TestNG |
| Automation | Selenium WebDriver 4.x |
| Driver management | WebDriverManager 5.x |
| Browser | Chrome |
| Design pattern | Page Object Model + PageFactory |
| Locators | XPath only (no CSS / ID / name locator strategies) |

## 3. Project Structure

```
SalesforceLoginFramework/
├── pom.xml
├── testng.xml
├── TEST_PLAN.md
└── src/
    ├── main/
    │   └── java/com/salesforce/framework/
    │       ├── config/ConfigReader.java
    │       ├── base/BaseTest.java
    │       └── pages/LoginPage.java
    └── test/
        ├── java/com/salesforce/tests/
        │   ├── ValidLoginTest.java
        │   └── InvalidLoginTest.java
        └── resources/config.properties
```

## 4. Test Environment Setup

1. Configure credentials in `src/test/resources/config.properties`:
   - `username=<external username>`
   - `password=<external password>`
2. Adjust `browser`, `implicit.wait`, `explicit.wait` as needed.
3. Configure the post-login landing-page verifier `home.page.verifier` if your org's home page differs.
4. Run from the project root: `mvn clean test`.

## 5. Test Case Matrix

| TC ID | Test Name | Data | Expected Result |
|-------|-----------|------|-----------------|
| TC01 | testValidLogin | Valid username + valid password from config | Redirected to authenticated Salesforce home page; verifier locator visible |
| TC02 | testInvalidLogin (empty/empty) | `""`, `""` | Error "Please enter your username." displayed |
| TC03 | testInvalidLogin (valid/empty) | valid username, `""` | Error "Please enter your password." displayed |
| TC04 | testInvalidLogin (invalid format/any) | malformed username, any password | "Please check your username and password..." displayed |
| TC05 | testInvalidLogin (wrong user/pass) | wrong username, wrong password | "Please check your username and password..." displayed |
| TC06 | testRememberMeCheckboxToggle | — | Checkbox toggles between selected and deselected on each click |

## 6. Test Execution

- **Valid login (TC01):** Requires real credentials in `config.properties`. Without them, the test fails fast with a clear configuration assertion message.
- **Invalid login (TC02–TC05):** Run without any credentials; data-driven via TestNG `@DataProvider`.
- **Remember me (TC06):** Pure UI-state test, no credentials required.

## 7. Standards & Constraints

- Page Object Model with `PageFactory`, `@FindBy`, constructor initialization, reusable action methods.
- XPath-only locators throughout.
- No `Thread.sleep()` — implicit waits (driver level) + explicit `WebDriverWait` (page actions).
- Structured try-catch exception handling in both the Page Object and test scripts; failures carry diagnostic page state (URL, error text).
- Setup/teardown via `@BeforeTest` / `@AfterTest`; screenshot on failure via `@AfterMethod`.
- No code comments (per prompt requirements); self-documenting method names.

## 8. Entry / Exit Criteria

**Entry:** Maven + Java 17+ installed, Chrome available, credentials configured for TC01.

**Exit:** All TC02–TC06 pass without credentials; TC01 passes with valid credentials; no `Thread.sleep`/comments in sources; XPath-only locators verified.
