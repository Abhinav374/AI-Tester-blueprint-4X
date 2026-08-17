import 'dotenv/config';

export interface AppConfig {
  baseUrl: string;
  email: string;
  password: string;
  navigationTimeoutMs: number;
  assertionTimeoutMs: number;
}

function optionalEnv(name: string): string {
  const value = process.env[name];
  return value ? value.trim() : '';
}

function requireEnv(name: string): string {
  const value = optionalEnv(name);
  if (!value) {
    throw new Error(
      `Environment variable ${name} is not set. Provide it via .env or the shell to run credential-dependent tests.`
    );
  }
  return value;
}

export function readConfig(): AppConfig {
  return {
    baseUrl: optionalEnv('VWO_BASE_URL') || 'https://app.vwo.com/#/login',
    email: optionalEnv('VWO_EMAIL'),
    password: optionalEnv('VWO_PASSWORD'),
    navigationTimeoutMs: 30000,
    assertionTimeoutMs: 15000,
  };
}

export function requireCredentials(config: AppConfig): { email: string; password: string } {
  return {
    email: requireEnv('VWO_EMAIL') || config.email,
    password: requireEnv('VWO_PASSWORD') || config.password,
  };
}
