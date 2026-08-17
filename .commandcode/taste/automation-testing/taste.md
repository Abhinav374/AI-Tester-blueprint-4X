# Taste

## Selenium / QA automation
- Standard web-automation stack: Selenium with Java, Maven, and TestNG. Confidence: 0.7
- Prefers XPath-only locators in Selenium; forbids CSS selectors, By.id, and By.name. Confidence: 0.9
- Prefers explicit WebDriverWait or implicit waits over Thread.sleep everywhere. Confidence: 0.9
- Prefers Page Object Model with PageFactory (@FindBy, constructor initialization) and reusable action methods. Confidence: 0.9
- Prefers TestNG annotations (@Test, @BeforeTest, @AfterTest) with shared setup/teardown logic. Confidence: 0.8
- Prefers structured try-catch exception handling in both page objects and test scripts. Confidence: 0.8
- Prefers externalizing URLs and credentials to a config file rather than hardcoding them; works against external/staging environments with credentials supplied separately (e.g., "I will give you the external username and password"). Confidence: 0.8
