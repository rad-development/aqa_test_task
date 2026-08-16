class EndpointProvider:

    @staticmethod
    def get_endpoints(endpoints_str: str, file_path: str) -> list[str]:
        if endpoints_str:
            endpoints = endpoints_str.split(",")
        else:
            with open(file_path, "r", encoding="utf-8") as file:
                endpoints = file.read().splitlines()

        endpoints = [endpoint.strip() for endpoint in endpoints]

        return endpoints
    