from dataclasses import dataclass
from enum import Enum


class Status(Enum):
    SUCCESS = "success"
    FAILED = "failed"
    ERROR = "error"
    OTHER = "other"


@dataclass
class CheckResult:
    endpoint: str
    status: Status
    elapsed: float | None
