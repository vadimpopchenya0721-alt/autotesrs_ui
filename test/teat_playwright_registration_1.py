from playwright.sync_api import sync_playwright, expect,Page
import pytest

def test_registration(chromium_page:Page):


        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input_registration = chromium_page.locator('//input[@id =":r0:"]')
        email_input_registration.fill("test@mail.ru")

        user_name_input = chromium_page.locator('//input[@id =":r1:"]')
        user_name_input.fill("test")

        password_input_registration = chromium_page.locator('//input[@id=":r2:"]')
        password_input_registration.fill("12345")

        click_registration = chromium_page.get_by_test_id('registration-page-registration-button')
        click_registration.click()

        dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard_title).to_have_text("Dashboard")



        dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard_title).to_be_visible()