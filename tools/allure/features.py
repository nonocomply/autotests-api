from enum import Enum


class AllureFeature(str, Enum):
    USERS = "Users"
    FILES = "Files"
    COURSES = "Courses"
    EXERCISES = "Exercises"
    AUTHENTICATION = "Authentication"


if __name__ == "__main__":
    pass
