from typing import TypedDict

import allure
from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.routes import APIRoutes


class PublicUsersClient(APIClient):
    """
    Клиент для работы с методами /api/v1/ysers, которые не требуют авторизации.
    """

    @allure.step("Create user")
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод создает нового пользователя.

        :param request: Словарь с email, password, lastName, firstName, middleName
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(APIRoutes.USERS, json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())


if __name__ == "__main__":
    pass
