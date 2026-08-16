from dataclasses import dataclass, field
from models.check_result import CheckResult, Status


@dataclass
class EndpointStats:
    success: int = 0
    failed: int = 0
    errors: int = 0
    other: int = 0
    response_times: list[float] = field(default_factory=list)

    def add(self, result: CheckResult):
        if result.status == Status.SUCCESS:
            self.success += 1
        elif result.status == Status.FAILED:
            self.failed += 1
        elif result.status == Status.ERROR:
            self.errors += 1
        elif result.status == Status.OTHER:
            self.other += 1

        if result.elapsed is not None:
            self.response_times.append(result.elapsed)
