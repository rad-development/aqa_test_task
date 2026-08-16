from concurrent.futures import ThreadPoolExecutor

from utils.argument_parser import ArgumentParser
from utils.endpoint_provider import EndpointProvider
from utils.endpoint_validator import EndpointValidator
from utils.http_checker import HttpChecker
from utils.report_generator import ReportGenerator


THREAD_COUNT = 5

def http_benchmark():
    # Получаем аргументы командной строки и парсим
    args = ArgumentParser.parse_arguments()
    endpoints = EndpointProvider.get_endpoints(args.hosts, args.file)
    EndpointValidator.validate_endpoints(endpoints)

    # Создаём список задач, для каждого endpoint отправляем count запросов
    tasks = [
        endpoint
        for endpoint in endpoints
        for _ in range(args.count)
    ]

    # Выполняем запросы параллельно в несколько потоков
    with ThreadPoolExecutor(max_workers=THREAD_COUNT) as executor:
        results = executor.map(HttpChecker.check, tasks)

    # Собираем отчет по результатам запросов
    report = ReportGenerator.generate(results)

    # Выводим отчет в консоль или в файл, в зависимости от аргументов запуска
    if args.output:
        with open(args.output, "w", encoding="utf-8") as file:
            file.write(report)
    else:
        print(report)

if __name__ == "__main__":
    http_benchmark()
