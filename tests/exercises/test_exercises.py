from http import HTTPStatus

import pytest

from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExerciseResponseSchema,
)
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import (
    assert_create_exercise_response,
    assert_get_exercise_response,
)
from tools.assertions.files import assert_get_file_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercise(
        self, exercises_client: ExercisesClient, function_course: CourseFixture
    ):
        request = CreateExerciseRequestSchema(
            course_id=function_course.response.course.id
        )
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)

        validate_json_schema(
            response.json(), CreateExerciseResponseSchema.model_json_schema()
        )

    def test_get_exercise(
        self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture
    ):
        exercise_id = function_exercise.response.exercise.id
        response = exercises_client.get_exercise_api(exercise_id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(response_data, function_exercise.response)

        validate_json_schema(
            response.json(), GetExerciseResponseSchema.model_json_schema()
        )


if __name__ == "__main__":
    pass
