import os
from datetime import datetime


def create_date_directories(date_list: list[datetime]) -> None:

    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    for dt in date_list:
        year_str = str(dt.year)
        month_str = f"{dt.month:02d}"
        day_str = f"{dt.day:02d}"

        year_path = os.path.join(base_dir, year_str)
        if not os.path.exists(year_path):
            os.mkdir(year_path)

        month_path = os.path.join(year_path, month_str)
        if not os.path.exists(month_path):
            os.mkdir(month_path)

        day_path = os.path.join(month_path, day_str)
        if not os.path.exists(day_path):
            os.mkdir(day_path)


def main() -> None:
    dates = [
        datetime(2019, 9, 2),
        datetime(2019, 7, 2),
        datetime(2019, 9, 15),
        datetime(2020, 1, 1),
        datetime(2020, 1, 10),
        datetime(2020, 5, 20),
        datetime(2021, 3, 8),
        datetime(2021, 3, 15),
        datetime(2021, 12, 31),
        datetime(2022, 2, 23),
        datetime(2022, 6, 1),
        datetime(2022, 6, 15),
        datetime(2023, 4, 12),
        datetime(2023, 4, 30),
        datetime(2023, 9, 1),
        datetime(2024, 1, 7),
        datetime(2024, 5, 9),
        datetime(2024, 11, 4),
        datetime(2025, 8, 22),
        datetime(2026, 10, 12),
    ]

    create_date_directories(dates)
    print("Директории успешно созданы.")


if __name__ == "__main__":
    main()