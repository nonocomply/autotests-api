import allure

from httpx import Request, Response

from tools.http.curl import make_curl_from_request
from tools.logger import get_logger

logger = get_logger("HTTP_CLIENT")


def curl_event_hook(request: Request):
    """
    Event hook для автоматического прикрепления cURL команды к Allure отчету.

    :param request: HTTP-запрос, переданный в `httpx` клиент.
    """
    # Генерируем команду cURL из объекта запроса
    curl_command = make_curl_from_request(request)

    # Прикрепляем сгенерированную cURL команду к отчету Allure
    allure.attach(
        curl_command, name="cURL command", attachment_type=allure.attachment_type.TEXT
    )


def log_request_event_hook(request: Request):
    """
    Логирует информацию об отправленном HTTP-запросе.

    :param request: Объект запроса HTTPX.
    """
    logger.info(f"Make {request.method} request to {request.url}")


def log_response_event_hook(response: Response):
    """
    Логирует информацию о полученном HTTP-ответе.

    :param response: Объект ответа HTTPX.
    """
    logger.info(
        f"Got response {response.status_code} {response.reason_phrase} from {response.url}"
    )


if __name__ == "__main__":
    pass
