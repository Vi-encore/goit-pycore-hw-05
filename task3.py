# optional
import sys
from typing import Dict, Callable, List
from collections import defaultdict


# Decorator for handling errors
def handle_errors(func: Callable) -> Callable:
    def inner_handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print("Помилка! Вказаний файл не було знайдено.")
            sys.exit(1)
        except ValueError as e:
            print(f"Помилка! Неправильно формат лог файлу. {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Непередбачена помилка!. {e}")
            sys.exit(1)

    return inner_handler


@handle_errors
# Parse file into list
def load_logs(file_path: str) -> list:
    with open(file_path, mode="r", encoding="utf-8") as fh:
        return [parse_log_line(line) for line in fh if line.strip()]


@handle_errors
# Create dict from line from file
def parse_log_line(line: str) -> dict:
    date, timestamp, level, *message = line.strip().split(" ")

    return {
        "date": date,
        "timestamp": timestamp,
        "level": level,
        "message": " ".join(message),
    }


# For counting how many levels of logs in file
def count_logs_by_level(logs: list) -> Dict[str, int]:
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1
    return dict(counts)


# To return logs for described log level
def filter_logs_by_level(logs: list, level: str) -> List[Dict[str, str]]:
    return list(filter(lambda log: log["level"].lower() == level.lower(), logs))


# To display info about logs
def display_log_count(counts: Dict[str, int]) -> None:
    print(f"{'Level':<15}{'Count':<10}")
    print("-" * 25)
    for level, count in counts.items():
        print(f"{level:<15}{count:<10}")


# To display specific logs for required level
def display_filtered_log_count(filtered_counts: Dict[str, str], level: str) -> None:
    print(f"\nДеталі логів для рівня {level.upper()}:")
    for log in filtered_counts:
        print(f"{log['date']} {log['timestamp']} - {log['message']}")


def main():
    try:
        file_path = sys.argv[1]
        level = sys.argv[2] if len(sys.argv) > 2 else None

        logs = load_logs(file_path)
        counts = count_logs_by_level(logs)
        display_log_count(counts)

        if level:
            filtered_counts = filter_logs_by_level(logs, level)
            display_filtered_log_count(filtered_counts, level)

    except IndexError:
        print("Помилка! Вкажіть шлях до файлу!")
        print("Використання: python task3.py <log_file_path> [level]")
        sys.exit(1)


if __name__ == "__main__":
    main()
