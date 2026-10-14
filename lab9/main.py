import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfReader


class PDFViewerApp(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:

        super().__init__(master)
        self.master = master
        self.reader: PdfReader | None = None
        self.current_page: int = 0
        self.total_pages: int = 0

        self.init_window()
        self.init_widgets()

    def init_window(self) -> None:
        """Настройка окна (заголовок и геометрия из теории)."""
        self.master.title("Просмотрщик PDF файлов")
        self.master.geometry("700x550")
        self.pack(fill=tk.BOTH, expand=True)

    def init_widgets(self) -> None:
        """Создание панели управления и текстовой области."""

        toolbar = tk.Frame(self)
        toolbar.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        btn_open = tk.Button(
            toolbar, text="Открыть PDF", command=self.open_pdf_file
        )
        btn_open.pack(side=tk.LEFT, padx=3)

        self.btn_prev = tk.Button(
            toolbar,
            text="< Назад",
            command=self.show_prev_page,
            state=tk.DISABLED,
        )
        self.btn_prev.pack(side=tk.LEFT, padx=3)

        self.btn_next = tk.Button(
            toolbar,
            text="Вперед >",
            command=self.show_next_page,
            state=tk.DISABLED,
        )
        self.btn_next.pack(side=tk.LEFT, padx=3)

        self.lbl_page = tk.Label(toolbar, text="Страница: 0 / 0")
        self.lbl_page.pack(side=tk.LEFT, padx=10)

        self.text_display = tk.Text(self, wrap=tk.WORD, font=("Arial", 11))
        self.text_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def open_pdf_file(self) -> None:
        """Диалог выбора PDF-файла и загрузка первой страницы."""
        file_path = filedialog.askopenfilename(
            filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
        )
        if not file_path:
            return

        try:
            self.reader = PdfReader(file_path)
            self.total_pages = len(self.reader.pages)
            self.current_page = 0
            self.render_page()
        except Exception as err:
            messagebox.showerror("Ошибка", f"Не удалось открыть PDF:\n{err}")

    def render_page(self) -> None:
        """Вывод текста текущей страницы в виджет Text."""
        if not self.reader:
            return

        page = self.reader.pages[self.current_page]
        text_content = page.extract_text() or "[Страница пуста или содержит только сканы/изображения]"


        self.text_display.delete("1.0", tk.END)
        self.text_display.insert(tk.END, text_content)

        self.lbl_page.config(
            text=f"Страница: {self.current_page + 1} / {self.total_pages}"
        )
        self.btn_prev.config(
            state=tk.NORMAL if self.current_page > 0 else tk.DISABLED
        )
        self.btn_next.config(
            state=(
                tk.NORMAL
                if self.current_page < self.total_pages - 1
                else tk.DISABLED
            )
        )

    def show_prev_page(self) -> None:
        if self.reader and self.current_page > 0:
            self.current_page -= 1
            self.render_page()

    def show_next_page(self) -> None:
        if self.reader and self.current_page < self.total_pages - 1:
            self.current_page += 1
            self.render_page()


def main() -> None:
    root = tk.Tk()
    app = PDFViewerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()