import argparse
import re
from pathlib import Path


class ArgumentValidator:
    MAX_REQUEST_COUNT = 1000

    @staticmethod
    def validate_input_file_path(file_path):
        # Проверяем формат пути к файлу
        file_path_pattern = re.compile(
            r"(?:[^\\/]+[\\/])*"
            r"[^\\/]+"
            r"\.txt"
        )
        if not file_path_pattern.fullmatch(file_path):
            raise argparse.ArgumentTypeError(
                f"Некорректный формат файла: {file_path}. "
                f"Ожидается файл с расширением .txt"
            )

        path = Path(file_path)

        # Проверяем существует ли путь
        if not path.exists():
            raise argparse.ArgumentTypeError(
                f"Файл не существует: {file_path}"
            )

        # Проверяем является ли путь файлом
        if not path.is_file():
            raise argparse.ArgumentTypeError(
                f"Указанный путь не является файлом: {file_path}"
            )

        return file_path

    @staticmethod
    def validate_output_file_path(file_path):
        # Проверяем формат пути к файлу
        file_path_pattern = re.compile(
            r"(?:[^\\/]+[\\/])*"
            r"[^\\/]+"
            r"\.txt"
        )
        if not file_path_pattern.fullmatch(file_path):
            raise argparse.ArgumentTypeError(
                f"Некорректный формат файла: {file_path}. "
                f"Ожидается файл с расширением .txt"
            )

        path = Path(file_path)
        parent_dir = path.parent

        # Проверяем существует ли директория
        if not parent_dir.exists():
            raise argparse.ArgumentTypeError(
                f"Директория не существует: {parent_dir}"
            )

        # Проверяем является ли путь директорией
        if not parent_dir.is_dir():
            raise argparse.ArgumentTypeError(
                f"Путь не является директорией: {parent_dir}"
            )

        return file_path

    @staticmethod
    def validate_count(count):
        # Проверяем является ли количество целым числом
        try:
            count = int(count)
        except ValueError:
            raise argparse.ArgumentTypeError(
                "Количество запросов должно быть целым числом"
            )

        # Проверяем допустимый диапазон количества запросов
        if not 1 <= count <= ArgumentValidator.MAX_REQUEST_COUNT:
            raise argparse.ArgumentTypeError(
                f"Количество запросов должно быть от 1 "
                f"до {ArgumentValidator.MAX_REQUEST_COUNT}"
            )

        return count