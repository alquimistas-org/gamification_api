import enum


class Status(enum.Enum):
    ACTIVE = "active"
    COMPLETED = "completed"


class UserRole(enum.Enum):
    ADMIN = "admin"
    USER = "user"
