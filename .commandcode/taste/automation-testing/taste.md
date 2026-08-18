# Taste

## Selenium / QA automation
- Standard web-automation stack: Selenium with Java, Maven, and TestNG. Confidence: 0.7
- Prefers XPath-only locators in Selenium; forbids CSS selectors, By.id, and By.name. Confidence: 0.9
- Prefers explicit WebDriverWait or implicit waits over Thread.sleep everywhere. Confidence: 0.9
- Prefers Page Object Model with PageFactory (@FindBy, constructor initialization) and reusable action methods. Confidence: 0.9
- Prefers TestNG annotations (@Test, @BeforeTest, @AfterTest) with shared setup/teardown logic. Confidence: 0.8
- Prefers structured try-catch exception handling in both page objects and test scripts. Confidence: 0.8
- Prefers externalizing URLs and credentials to a config file rather than hardcoding them; works against external/staging environments with credentials supplied separately (e.g., "I will give you the external username and password"). Confidence: 0.8

## Playwright (TypeScript)
- When using Playwright + TypeScript, prefers accessibility-first locators (getByRole, getByPlaceholder, getByLabel, getByText) over CSS/XPath/ID selectors — mirroring the Selenium XPath-only rule; resolves ambiguous multi-match locators with `.first()`. Confidence: 0.8
- Prefers probing/verifying the live application page to confirm real locators, error-message text, and element behavior (e.g., hidden checkboxes) before finalizing the framework and assertions. Confidence: 0.7
- Prefers supplying external credentials via environment variables (no secrets committed), with credential-dependent tests skipping gracefully when the credentials are absent. Confidence: 0.7
