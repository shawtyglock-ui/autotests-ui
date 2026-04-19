from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.course_menu_button = page.get_by_test_id('course-view-menu-button')
        self.course_edit_menu_item = page.get_by_test_id('course-view-edit-menu-item')
        self.course_delete_menu_item = page.get_by_test_id('course-view-delete-menu-item')

    def click_edit_course(self, index: int):
        self.course_menu_button.nth(index).click()

        # После нажатия на кнопку меню обязательно проверяем, что меню открылась и меню айтем виден
        expect(self.course_edit_menu_item.nth(index)).to_be_visible()
        self.course_edit_menu_item.nth(index).click()

    def click_delete_course(self, index: int):
        self.course_menu_button.nth(index).click()

        expect(self.course_delete_menu_item.nth(index)).to_be_visible()
        self.course_delete_menu_item.nth(index).click()
