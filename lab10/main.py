import matplotlib.pyplot as plt
import numpy as np


def visualize_array_with_zeros(numbers: list[int]) -> None:
    arr = np.array(numbers)
    x_indices = np.arange(len(arr))

    zero_mask = arr == 0
    zero_x = x_indices[zero_mask]
    zero_y = arr[zero_mask]

    plt.figure(figsize=(8, 4.5))

    plt.plot(x_indices, arr, label="Значения массива", color="blue", alpha=0.7)

    if len(zero_x) > 0:
        plt.scatter(
            zero_x,
            zero_y,
            color="red",
            s=100,
            zorder=5,
            label=f"Нули (всего: {len(zero_x)})",
        )

        for x, y in zip(zero_x, zero_y):
            plt.text(
                x,
                y + 0.3,
                "0",
                ha="center",
                color="red",
                fontweight="bold",
            )

    plt.axhline(0, color="gray", linestyle="--", linewidth=0.8)
    plt.grid(True)

    # 6. Подписи и легенда
    plt.title("Визуализация массива с выделением нулевых значений")
    plt.xlabel("Индекс элемента")
    plt.ylabel("Значение")
    plt.legend()

    plt.show()


def main() -> None:
    test_data = [4, 2, 0, -3, -1, 0, 5, 3, 0, 2]
    visualize_array_with_zeros(test_data)


if __name__ == "__main__":
    main()