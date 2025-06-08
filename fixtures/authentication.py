import pytest

from clients.authentication.authentication_client import (
    get_authentication_client,
    AuthenticationClient,
)


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    # Создаем новый API клиент для работы с аутентификацией
    return get_authentication_client()


if __name__ == "__main__":
    pass
