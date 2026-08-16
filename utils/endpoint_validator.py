import argparse
import re

class EndpointValidator:

    @staticmethod
    def validate_endpoint_format(endpoint):
        endpoint_pattern = re.compile(
            r"https?://"             # протокол http или https
            r"[a-zA-Z0-9-]+"         # имя домена
            r"(?:\.[a-zA-Z0-9-]+)+"  # доменная зона (.com, .ru, .co.uk и т.д.)
            r"(?::[0-9]+)?"          # необязательный порт
            r"(?:/.*)?"              # необязательный путь
        )
        if not endpoint_pattern.fullmatch(endpoint):
            raise argparse.ArgumentTypeError(
                f"Некорректный URL: {endpoint}"
            )
        return endpoint

    @staticmethod
    def validate_endpoints(endpoints: list[str]) -> list[str]:
        for endpoint in endpoints:
            EndpointValidator.validate_endpoint_format(endpoint)
        return endpoints
