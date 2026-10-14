def shift_characters(text: str) -> str:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    limit_index = alphabet.index("ы") 

    shifted_list = list(
        alphabet[alphabet.index(char.lower()) + 1]
        if char.lower() in alphabet[:limit_index]
        else char
        for char in text
    )

    return "".join(shifted_list)


def main() -> None:
    test_string = "абвгдеыэюя! Привет"
    result = shift_characters(test_string)

    print("Исходная строка:", test_string)
    print("Результат:      ", result)


if __name__ == "__main__":
    main()