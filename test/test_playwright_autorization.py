import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization():
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        page = chromium.new_page()
        page.goto(" https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
        email_input.fill("test@mail.ru")

        password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
        password_input.fill("test")

        login_button = page.locator('//button[@data-testid="login-page-login-button"]')
        login_button.click()

        wrong_email_or_password_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
        expect(wrong_email_or_password_alert).to_be_visible()

        expect(wrong_email_or_password_alert).to_have_text("Wrong email or password ")
