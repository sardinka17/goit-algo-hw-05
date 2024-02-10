import sys


def process_error(func):
    def inner():
        try:
            return func()
        except IndexError:
            print("Invalid arguments.")
        except FileNotFoundError:
            print("File not found.")
        except (ValueError, TypeError, AttributeError):
            print("File format is not correct.")

    return inner


def parse_input() -> tuple[str, str]:
    path: str = sys.argv[1]
    level: str = sys.argv[2].upper() if len(sys.argv) > 2 else None

    return path, level


def parse_log_line(line: str) -> dict:
    date, time, level, *words = line.replace("\n", "").split()
    log_dict = {"date": date, "time": time, "level": level, "message": " ".join(words)}

    return log_dict


def load_logs(file_path: str) -> list:
    logs = []

    with open(file_path, "r", encoding="utf-8") as file_log:
        while True:
            line = file_log.readline()

            if not line:
                break

            logs.append(parse_log_line(line))

    return logs


def count_logs_by_level(logs: list) -> dict:
    logs_by_level = {}

    for log in logs:
        level = log["level"]

        if level in logs_by_level:
            logs_by_level[level] += 1
        else:
            logs_by_level[level] = 1

    return logs_by_level


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for key, value in counts.items():
        print(f"{key}{' ' * (17 - len(key))}| {value}")


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"] == level, logs))


def display_logs_by_level(logs: list, level: str):
    if len(logs) == 0:
        print(f"{level} level is invalid.")
        return

    print(f"\nДеталі логів для рівня '{level}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


@process_error
def main():
    path, level = parse_input()
    logs = load_logs(path)
    logs_by_level = count_logs_by_level(logs)

    display_log_counts(logs_by_level)

    if level is not None:
        filtered_logs = filter_logs_by_level(logs, level)
        display_logs_by_level(filtered_logs, level)


if __name__ == "__main__":
    main()
