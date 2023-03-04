from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("500x400")

# функция для загрузки файла
def load_file():

    # получаем путь к загружаемому файлу
    file_path = filedialog.askopenfilename()

    # получаем содержимое файла
    with open(file_path, "r") as f:
        data = f.readlines()

    # обрабатываем содержимое файла
    processed_data = []
    for line in data:
        processed_data.append(prefix_entry.get() + line.strip() + postfix_entry.get() + "\n")

    # выводим результат обработки файла
    result_text.delete(1.0, END)
    result_text.insert(END, "".join(processed_data))

    # записываем обработанные данные в файл
    with open("processed_file.txt", "w") as f:
        f.writelines(processed_data)

# создаем поля для префикса и постфикса
prefix_label = Label(root, text="Префикс:")
prefix_label.pack()
prefix_entry = Entry(root)
prefix_entry.pack()

postfix_label = Label(root, text="Постфикс:")
postfix_label.pack()
postfix_entry = Entry(root)
postfix_entry.pack()

# создаем кнопку "Загрузить файл"
load_button = Button(root, text="Загрузить файл", command=load_file)
load_button.pack()

# создаем текстовое поле для вывода результата
result_label = Label(root, text="Результат:")
result_label.pack()
result_text = Text(root, height=10)
result_text.pack()

root.mainloop()
