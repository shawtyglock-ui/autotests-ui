from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.menu = CourseViewMenuComponent(page)
        self.course_title = page.get_by_test_id('course-widget-title-text')
        self.course_image = page.get_by_test_id('course-preview-image')
        self.course_max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.course_min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.course_estimated_time_text = page.get_by_test_id('course-estimated-time-info-row-view-text')

    def check_visible(
            self,
            index: int,  # Индекс карточки в списке курсов
            title: str,  # Ожидаемый заголовок курса
            max_score: str,  # Ожидаемый максимальный балл
            min_score: str,  # Ожидаемый минимальный балл
            estimated_time: str  # Ожидаемое время прохождения
    ):
        expect(self.course_image.nth(index)).to_be_visible()

        # Обратите внимание на использование метода nth, он позволяет получить локатор по индексу
        expect(self.course_title.nth(index)).to_be_visible()
        expect(self.course_title.nth(index)).to_have_text(title)

        expect(self.course_max_score_text.nth(index)).to_be_visible()
        expect(self.course_max_score_text.nth(index)).to_have_text(f"Max score: {max_score}")

        expect(self.course_min_score_text.nth(index)).to_be_visible()
        expect(self.course_min_score_text.nth(index)).to_have_text(f"Min score: {min_score}")

        expect(self.course_estimated_time_text.nth(index)).to_be_visible()
        expect(self.course_estimated_time_text.nth(index)).to_have_text(
            f"Estimated time: {estimated_time}"
        )
