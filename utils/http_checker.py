import requests 
import time 
from http import HTTPStatus 
from models.check_result import CheckResult, Status 
 
 
class HttpChecker: 
    DEFAULT_TIMEOUT = 5 
 
    @staticmethod 
    def check(endpoint: str, timeout: int | None = None) -> CheckResult: 
        if timeout is None: 
            timeout = HttpChecker.DEFAULT_TIMEOUT 
 
        try: 
            # Замеряем время и отправляем запрос
            start = time.perf_counter() 
            
            response = requests.get(endpoint, timeout=timeout) 
            
            elapsed = time.perf_counter() - start 
            
            status = HTTPStatus(response.status_code) 

            # Определяем результат запроса по его HTTP-статусу
            if status.is_success: 
                result = Status.SUCCESS 
            elif status.is_client_error or status.is_server_error: 
                result = Status.FAILED 
            else: 
                result = Status.OTHER 

            return CheckResult( 
                endpoint=endpoint, 
                status=result, 
                elapsed=elapsed 
            ) 
         
        except requests.exceptions.RequestException as error: 
            print(f"Не удалось подключиться к серверу {endpoint}, ошибка: {error}") 
            
            # Возвращаем результат с ошибкой подключения
            return CheckResult( 
                endpoint=endpoint, 
                status=Status.ERROR, 
                elapsed=None 
            )
        