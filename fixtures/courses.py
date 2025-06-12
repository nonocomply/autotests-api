import pytest
from pydantic import BaseModel

from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.courses.courses_schema import (
    CreateCourseResponseSchema,
    CreateCourseRequestSchema,
)
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema


@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(user=function_user.authentication_user)


@pytest.fixture
def function_course(
    courses_client: CoursesClient,
    function_user: UserFixture,
    function_file: FileFixture,
) -> CourseFixture:
    request = CreateCourseRequestSchema(
        preview_file_id=function_file.response.file.id,
        created_by_user_id=function_user.response.user.id,
    )
    response = courses_client.create_course(request=request)
    return CourseFixture(request=request, response=response)


if __name__ == "__main__":
    pass
