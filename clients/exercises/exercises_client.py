from typing import TypedDict, List

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class GetExerciseQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий.
    """

    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """

    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int | None
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление данных задания.
    """

    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class Exercise(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesResponseDict(TypedDict):
    exercises: List[Exercise]


class GetExerciseResponseDict(TypedDict):
    exercise: Exercise


class ExercisesClient(APIClient):
    def get_exercises_api(self, query: GetExerciseQueryDict) -> Response:
        """
        Метод для получения списка заданий для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод для создания задания.

        :param request:
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для получения информации о задании по exercise_id.

        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def update_exercise_api(
        self, exercise_id: str, request: UpdateExerciseRequestDict
    ) -> Response:
        """
        Метод для обновления данных задания.

        :param exercise_id: Идентификатор задания
        :param request:
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления задания.

        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, query: GetExerciseQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query=query)
        return response.json()

    def create_exercise(
        self, request: CreateExerciseRequestDict
    ) -> GetExerciseResponseDict:
        response = self.create_exercise_api(request=request)
        return response.json()

    def update_exercise(
        self, exercise_id: str, request: UpdateExerciseRequestDict
    ) -> GetExerciseResponseDict:
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return response.json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))


if __name__ == "__main__":
    pass
