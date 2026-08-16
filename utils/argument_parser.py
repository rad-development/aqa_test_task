import argparse
from utils.argument_validator import ArgumentValidator


class ArgumentParser:

    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser()

        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument(
            "-H", "--hosts",
            type=str
        )
        group.add_argument(
            "-F", "--file",
            type=ArgumentValidator.validate_input_file_path
        )

        parser.add_argument(
            "-C", "--count",
            type=ArgumentValidator.validate_count,
            default=1
        )
        parser.add_argument(
            "-O", "--output",
            type=ArgumentValidator.validate_output_file_path
        )

        return parser.parse_args()
