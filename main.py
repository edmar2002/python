import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")  # Получаем текущее время
    clock_label.config(text=current_time)     # Обновляем текст метки
    clock_label.after(1000, update_time)      # Обновляем каждую секунду

# Создаем окно
window = tk.Tk()
window.title("Онлайн часики")
window.geometry("3000x1500")

# Настраиваем стиль
clock_label = tk.Label(
    window,
    font=("Arial", 300, "bold"),
    bg="black",
    fg="white",
    padx=2000,
    pady=2000
)
clock_label.pack(expand=True)

# Запускаем обновление времени
update_time()

# Запускаем главный цикл
window.mainloop()