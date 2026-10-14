import os
from PIL import Image, UnidentifiedImageError


def create_thumbnails_in_directory(
    directory_path: str, size: tuple[int, int] = (128, 128)
) -> None:

    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Директория '{directory_path}' не найдена.")

    thumb_dir = os.path.join(directory_path, "thumbnail")
    os.makedirs(thumb_dir, exist_ok=True)

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        if not os.path.isfile(file_path):
            continue

        try:
            with Image.open(file_path) as img:

                img.thumbnail(size)

                output_path = os.path.join(thumb_dir, filename)
                img.save(output_path)
                print(f"Миниатюра создана: {output_path}")

        except (OSError, UnidentifiedImageError, SyntaxError):
            continue


def main() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(base_dir, "test_images")

    # Создаем тестовую папку и файлы, только если их нет
    if not os.path.exists(test_dir):
        os.makedirs(test_dir, exist_ok=True)

        img1 = Image.new("RGB", (800, 600), color="blue")
        img1.save(os.path.join(test_dir, "photo1.jpg"))

        img2 = Image.new("RGB", (1024, 768), color="green")
        img2.save(os.path.join(test_dir, "photo2.png"))

        with open(os.path.join(test_dir, "notes.txt"), "w", encoding="utf-8") as f:
            f.write("test")

    create_thumbnails_in_directory(test_dir)
    print("Обработка завершена.")


if __name__ == "__main__":
    main()