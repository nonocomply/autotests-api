from typing import TypedDict

import allure
from httpx import Response

from clients.api_client import APIClient
from clients.courses.courses_schema import (
    CreateCourseResponseSchema,
    CreateCourseRequestSchema,
    UpdateCourseRequestSchema,
    GetCoursesQuerySchema,
)
from clients.files.files_schema import FileSchema

from clients.private_http_builder import (
    get_private_http_client,
    AuthenticationUserSchema,
)
from clients.users.users_schema import UserSchema
from tools.routes import APIRoutes


class CoursesClient(APIClient):
    @allure.step("Get courses")
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(APIRoutes.COURSES, params=query.model_dump(by_alias=True))

    @allure.step("Get course by id {course_id}")
    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.COURSES}/{course_id}")

    @allure.step("Create course")
    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(APIRoutes.COURSES, json=request.model_dump(by_alias=True))

    @allure.step("Update course by id {course_id}")
    def update_course_api(
        self, course_id: str, request: UpdateCourseRequestSchema
    ) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(
            f"{APIRoutes.COURSES}/{course_id}", json=request.model_dump(by_alias=True)
        )

    @allure.step("Delete course by id {course_id}")
    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{APIRoutes.COURSES}/{course_id}")

    def create_course(
        self, request: CreateCourseRequestSchema
    ) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)


# Добавляем builder для CoursesClient
def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))


if __name__ == "__main__":
    pass
