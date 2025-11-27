from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://ortex.github.io/snils-generator/')
    snils = page.locator('//span[@class="number"]').inner_text()

    page.goto(
        'https://frloz-dev.helpms.ru/oauth2/authorization/admin-web')
    # Авторизация
    login_input = page.locator('//input[@id="username"]')
    login_input.fill('320-096-445 36')
    password_input = page.locator('//input[@id="password"]')
    password_input.fill('$987erpLKM@')
    login_button = page.locator('//button[@id="kc-login"]')
    login_button.click()

    frloz_header = page.locator('//button[@class="widget-card-button"]')
    frloz_header.click()

    add_register = page.locator('//button[@buttonid="frloz_mi5"]')
    add_register.click()

    choice_nozologiya = page.locator('//input[@label="Выбор заболевания и (или) состояния"]')
    choice_nozologiya.click()

    choice_nozologiya_ZNO = page.locator('//ul[@class="zireael-dropdown-options"]')
    choice_nozologiya_ZNO.click()

    choice_nozologiya_ZNO = page.locator('//button[@buttonid="frloz_frloz_mi5_mi0"]')
    choice_nozologiya_ZNO.click()







    page.wait_for_timeout(5000)
