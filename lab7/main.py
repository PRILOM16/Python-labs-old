class UserLanguagePreference:
    def __init__(self, languages_str: str) -> None:
        parsed_languages = [
            lang.strip() for lang in languages_str.split(",") if lang.strip()
        ]

        self.__languages: list[str] = []
        for lang in parsed_languages:
            if lang not in self.__languages:
                self.__languages.append(lang)

    def add_lang(self, lang_str: str) -> None:
        cleaned_lang = lang_str.strip()
        if cleaned_lang and cleaned_lang not in self.__languages:
            self.__languages.append(cleaned_lang)

    def get_languages(self) -> list[str]:
        return self.__languages.copy()


def main() -> None:
    user_pref = UserLanguagePreference("Python, English, Russian")
    print("Начальный список языков:", user_pref.get_languages())

    user_pref.add_lang("Python")
    print("После попытки добавить 'Python' снова:", user_pref.get_languages())

    user_pref.add_lang("German")
    print("После добавления 'German':", user_pref.get_languages())

    try:
        print(user_pref.__languages)
    except AttributeError:
        print("Прямой доступ к self.__languages закрыт (вызван AttributeError).")


if __name__ == "__main__":
    main()