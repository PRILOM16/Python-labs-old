def count_occurrences(items: list) -> dict:
    counts = {}

    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    return counts


def main() -> None:
    test_data = ["apple", "banana", "apple", "orange", "banana", "apple", "kiwi"]

    result = count_occurrences(test_data)
    print("Результат подсчета:")
    print(result)


if __name__ == "__main__":
    main()