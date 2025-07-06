const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests',
  timeout: 30000,
  use: {
    headless: true,
    baseURL: 'https://recruter.ai',
    ignoreHTTPSErrors: true,
  },
  reporter: [
    ["json", { outputFile: "results/test-results.json" }]
  ],
});