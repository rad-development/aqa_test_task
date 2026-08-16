from models.endpoint_stats import EndpointStats


class ReportGenerator:
    SEPARATOR = "-" * 30

    @staticmethod
    def generate(results) -> str:
        stats = {}

        # Собираем результаты запросов по каждому хосту
        for result in results:
            if result.endpoint not in stats:
                stats[result.endpoint] = EndpointStats()

            stats[result.endpoint].add(result)

        stats_lines = [ReportGenerator.SEPARATOR]

        # Формируем отчёт для каждого хоста
        for endpoint, data in stats.items():
            lines = [
                f"Host: {endpoint}",
                f"Success: {data.success}",
                f"Failed: {data.failed}",
                f"Errors: {data.errors}",
            ]

            # Если были запросы с измеренным временем, рассчитываем статистику
            if data.response_times:
                avg = sum(data.response_times) / len(data.response_times)
                lines.extend([
                    f"Min: {min(data.response_times):.3f} s",
                    f"Max: {max(data.response_times):.3f} s",
                    f"Avg: {avg:.3f} s",
                ])
                
            lines.append(ReportGenerator.SEPARATOR)
            stats_lines.extend(lines)

        # Объединяем все строки в единый отчёт
        report = "\n".join(stats_lines)

        return report
    