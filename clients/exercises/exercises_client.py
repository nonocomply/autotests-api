from typing import TypedDict, List

import allure
from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import (
    GetExerciseQuerySchema,
    UpdateExerciseRequestSchema,
    CreateExerciseRequestSchema,
    GetExerciseResponseSchema,
    GetExercisesResponseSchema,
    CreateExerciseResponseSchema,
)
from clients.private_http_builder import (
    get_private_http_client,
    AuthenticationUserSchema,
)


class ExercisesClient(APIClient):
    @allure.step("Get exercises")
    def get_exercises_api(self, query: GetExerciseQuerySchema) -> Response:
        """
        Метод для получения списка заданий для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод для создания задания.

        :param request:
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    @allure.step("Get exercise by id {exercise_id}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для получения информации о задании по exercise_id.

        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    @allure.step("Update exercise by id {exercise_id}")
    def update_exercise_api(
        self, exercise_id: str, request: UpdateExerciseRequestSchema
    ) -> Response:
        """
        Метод для обновления данных задания.

        :param exercise_id: Идентификатор задания
        :param request:
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(
            f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True)
        )

    @allure.step("Delete exercise by id {exercise_id}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления задания.

        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(
        self, query: GetExerciseQuerySchema
    ) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query=query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(
        self, request: CreateExerciseRequestSchema
    ) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request=request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(
        self, exercise_id: str, request: UpdateExerciseRequestSchema
    ) -> GetExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return GetExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))


if __name__ == "__main__":
    pass
