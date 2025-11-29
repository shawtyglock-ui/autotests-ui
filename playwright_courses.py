from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # Создание контекста
    page = context.new_page()  # Создание страницы

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    page.get_by_test_id('registration-form-email-input').locator('input').fill("user.name@gmail.com")
    page.get_by_test_id('registration-form-username-input').locator('input').fill("username")
    page.get_by_test_id("registration-form-password-input").locator('input').fill("password")
    page.get_by_test_id('registration-page-registration-button').click()
    context.storage_state(path="browser-state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    header_Courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(header_Courses).to_have_text('Courses')
    expect(header_Courses).to_be_visible()

    ikonka = page.get_by_test_id('courses-list-empty-view-icon')
    expect(ikonka).to_be_visible()

    text_Thereisnoresults = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(text_Thereisnoresults).to_have_text('There is no results')
    expect(text_Thereisnoresults).to_be_visible()

    text_Results = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(text_Results).to_have_text('Results from the load test pipeline will be displayed here')
    expect(text_Results).to_be_visible()

    page.wait_for_timeout(5000)
