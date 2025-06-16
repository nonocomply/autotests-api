from typing import Any

import allure
from jsonschema import validate
from jsonschema.validators import Draft202012Validator


@allure.step("Validate JSON schema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )


if __name__ == "__main__":
    pass
