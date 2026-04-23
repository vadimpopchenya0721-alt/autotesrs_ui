from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input_registration = page.locator('//input[@id =":r0:"]')
    email_input_registration.fill("test@mail.ru")

    user_name_input = page.locator('//input[@id =":r1:"]')
    user_name_input.fill("test")

    password_input_registration = page.locator('//input[@id=":r2:"]')
    password_input_registration.fill("12345")

    click_registration = page.get_by_test_id('registration-page-registration-button')
    click_registration.click()

    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_have_text("Dashboard")

