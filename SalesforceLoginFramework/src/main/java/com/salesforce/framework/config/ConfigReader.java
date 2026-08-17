package com.salesforce.framework.config;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public final class ConfigReader {

    private static final Properties properties = new Properties();
    private static final ConfigReader INSTANCE = new ConfigReader();

    private ConfigReader() {
        try (InputStream inputStream = ConfigReader.class.getClassLoader().getResourceAsStream("config.properties")) {
            if (inputStream == null) {
                throw new IllegalStateException("config.properties not found on the classpath");
            }
            properties.load(inputStream);
        } catch (IOException e) {
            throw new IllegalStateException("Failed to load config.properties", e);
        }
    }

    public static ConfigReader getInstance() {
        return INSTANCE;
    }

    public String getUrl() {
        return properties.getProperty("url");
    }

    public String getBrowser() {
        return properties.getProperty("browser");
    }

    public String getUsername() {
        return properties.getProperty("username");
    }

    public String getPassword() {
        return properties.getProperty("password");
    }

    public String getHomePageVerifier() {
        return properties.getProperty("home.page.verifier");
    }

    public int getImplicitWait() {
        return Integer.parseInt(properties.getProperty("implicit.wait"));
    }

    public int getExplicitWait() {
        return Integer.parseInt(properties.getProperty("explicit.wait"));
    }
}
