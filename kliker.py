import tkinter as tk

class ClickerGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Проста гра клікер")
        self.geometry("300x200")

        self.click_count = 0

        self.label = tk.Label(self, text="Клікни, щоб збільшити лічильник!")
        self.label.pack(pady=20)

        self.click_button = tk.Button(self, text="Клік!", command=self.on_click)
        self.click_button.pack()

        self.counter_label = tk.Label(self, text="Лічильник: 0")
        self.counter_label.pack(pady=10)

    def on_click(self):
        self.click_count += 1
        self.counter_label.config(text=f"Лічильник: {self.click_count}")

if __name__ == "__main__":
    app = ClickerGame()
    app.mainloop()