from http import HTTPStatus

import pytest

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExerciseResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
)
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import (
    assert_create_exercise_response,
    assert_get_exercise_response,
    assert_update_exercise_response,
    assert_exercise_not_found_response,
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

    def test_update_exercise(
        self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture
    ):
        exercise_id = function_exercise.response.exercise.id
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(exercise_id, request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request, response_data)

        validate_json_schema(
            response.json(), UpdateExerciseResponseSchema.model_json_schema()
        )

    def test_delete_exercise(
        self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture
    ):
        exercise_id = function_exercise.response.exercise.id
        response = exercises_client.delete_exercise_api(exercise_id)
        assert_status_code(response.status_code, HTTPStatus.OK)

        get_response = exercises_client.get_exercise_api(exercise_id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(
            get_response.text
        )
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(get_response_data)

        validate_json_schema(
            get_response.json(), InternalErrorResponseSchema.model_json_schema()
        )


if __name__ == "__main__":
    pass
