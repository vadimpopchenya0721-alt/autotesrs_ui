from playwright.sync_api import Page, expect
import pytest

from pages.course_list_page import CourseListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_courses(course_list_page: CourseListPage, create_course_page: CreateCoursePage, ):
    # Посещение страницы создания курса
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    create_course_page.check_visible_create_course_title()  # Проверка видимости заголовка "Создать курс"
    create_course_page.check_disabled_create_course_button()  # Кнопка создания курса неактивна
    create_course_page.check_visible_image_preview_empty_view()  # Пустой просмотр превью изображения
    create_course_page.check_visible_create_course_form("", "", "", "0", "0")  # Проверка формы создания
    create_course_page.check_visible_exercises_title()  # Заголовок "Упражнения" виден
    create_course_page.check_visible_create_exercise_button()  # Кнопка "Создать упражнение" видна
    create_course_page.check_visible_exercises_empty_view()  # Пустой список упражнений

    create_course_page.upload_preview_image("./testdata/files/image.png")  # Загрузка превью
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)  # Изображение загружено

    # Заполнение формы создания курса
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    create_course_page.click_create_course_button()  # Нажатие кнопки создания курса

    # Проверки на странице списка курсов
    course_list_page.check_visible_courses_title()  # Заголовок "Курсы" виден
    course_list_page.click_create_course_button()  # Клик по кнопке создания курса
    course_list_page.check_visible_course_card(  # Проверка карточки курса
        index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
    )
    course_list_page.click_create_course_button()
    course_list_page.check_visible_courses_title()
    course_list_page.check_visible_create_course_button()
    course_list_page.check_visible_course_card(
        index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
    )


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):  # тест_пустого_списка_курсов
    # Переход на страницу списка курсов
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверка заголовка страницы
    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()  # Заголовок виден
    expect(courses_title).to_have_text('Courses')  # Текст заголовка "Courses"

    # Проверка иконки пустого состояния
    empty_view_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()

    # Проверка заголовка пустого состояния
    empty_view_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_view_title).to_be_visible()
    expect(empty_view_title).to_have_text('There is no results')  # "Нет результатов"

    # Проверка описания пустого состояния
    empty_view_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_view_description).to_be_visible()
    expect(empty_view_description).to_have_text('Results from the load test pipeline will be displayed here')
    # "Здесь будут отображаться результаты конвейера нагрузочного тестирования"