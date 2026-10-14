def sum_numeric_strings(strings: list[str]) -> float:
    return sum(float(item) for item in strings)


def main() -> None:
    test_data = ["10", "3.5", "-2", "0.75", "42"]

    total = sum_numeric_strings(test_data)

    print("Исходный список:", test_data)
    print("Сумма элементов:", total)


if __name__ == "__main__":
    main()