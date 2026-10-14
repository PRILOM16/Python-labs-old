import os
import json

def read_first_n_lines(file_path: str, count: int) -> list[str]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл по пути '{file_path}' не найден.")

    lines: list[str] = []
    with open(file_path, "r", encoding="utf-8") as file:
        for _ in range(count):
            line = file.readline()
            if not line:
                break
            lines.append(line.strip()) 

    return lines


def main() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))

    test_file_path = os.path.join(base_dir, "example.txt")
    json_file_path = os.path.join(base_dir, "result.json")

    with open(test_file_path, "w", encoding="utf-8") as file:
        file.write("Первая строка\n")
        file.write("Вторая строка\n")
        file.write("Третья строка\n")
        file.write("Четвертая строка\n")

    lines_to_read = 3
    result = read_first_n_lines(test_file_path, lines_to_read)
    
    with open(json_file_path, "w", encoding="utf-8") as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)

    print(f"Считано строк ({len(result)}).")
    print(f"Результат успешно сохранен в '{json_file_path}'.")


if __name__ == "__main__":
    main()