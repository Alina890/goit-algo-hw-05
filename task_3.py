from pathlib import Path
from collections import defaultdict
import sys

file_path = Path("file.txt")
with open(file_path, 'w',encoding= "UTF-8") as fh:
    fh.write ("2024-01-22 08:30:01 INFO User logged in successfully.\n2024-01-22 08:45:23 DEBUG Attempting to connect to the database.\n2024-01-22 09:00:45 ERROR Database connection failed.\n2024-01-22 09:15:10 INFO Data export completed.\n2024-01-22 10:30:55 WARNING Disk usage above 80%.\n2024-01-22 11:05:00 DEBUG Starting data backup process.\n2024-01-22 11:30:15 ERROR Backup process failed.\n2024-01-22 12:00:00 INFO User logged out.\n2024-01-22 12:45:05 DEBUG Checking system health.\n2024-01-22 13:30:30 INFO Scheduled maintenance.")


def parse_log_line(line: str) -> dict:
        lines = line.split(" ", maxsplit=5)
        date, time, level, message = lines[0], lines[1], lines[2], " ".join(lines[3:])
        return {"date": date,"time": time,"level": level,"message": message.strip()}
           

def load_logs(file_path: str) -> list:
    logs_list = []
    try:
        with open(file_path,'r',encoding= "UTF-8") as fh:
            for line in fh:
                logs_list.append(parse_log_line(line))
    except FileNotFoundError:
        print (f"Файл {file_path} не знайдено.")
    except Exception as e:
        print(f"Сталась помилка при читанні файлу: {e}")
    return logs_list


def filter_logs_by_level(logs: list, level: str) -> list:
    return [value for value in logs if value["level"] == level.upper()]


def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for value in logs:
        counts[value["level"]] += 1
    return counts


def display_log_counts(counts: dict):
    print("Статистика рівнів логування:")
    for level, count in counts.items():
        print(f"{level}: {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використання: python script.py <шлях_до_файлу_логів> [рівень_логування]")
        sys.exit(1)

file_path = sys.argv[1]
logs = load_logs(file_path)

if len(sys.argv) == 3:
    level = sys.argv[2]
    filtered_logs = filter_logs_by_level(logs, level)
    log_counts = count_logs_by_level(filtered_logs)
    display_log_counts(log_counts)
else:
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)


#python [main.py](<http://main.py/>) /path/to/logfile.log
#python main.py path/to/logfile.log error

