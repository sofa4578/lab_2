from tkinter import *
from random import choice
import string
import os
import sys

# Функція для коректної роботи з ресурсами (зображенням/іконкою) у .exe
def resource_path(relative_path):
    """ Отримати абсолютний шлях до ресурсу в .exe або IDE """
    try:
        base_path = sys._MEIPASS  # шлях тимчасової папки у .exe
    except AttributeError:
        base_path = os.path.abspath(".")  # шлях при запуску з IDE

    return os.path.join(base_path, relative_path)

class App:
    def __init__(self):
        self.window = Tk()
        self.window.title('password_generator')
        self.window.iconbitmap(resource_path('logo.ico'))
        self.window.iconphoto(False, PhotoImage(file=resource_path('logo.png')))
        self.window.geometry('500x255')
        self.window.config(bg='gray')

        # створення компонентів
        self.label()
        self.entry()
        self.button()

    def label(self):
        label_title = Label(self.window, text='Welcome to password generator', font=('Courier', 20), bg='gray', fg='black')
        label_title.pack()

    def entry(self):
        self.password_entry = Entry(self.window, font=('Courier', 25), bg='white', fg='black', width=30, relief='solid')
        self.password_entry.pack(pady=50)

    def button(self):
        password_generator = Button(self.window, text="Generate password", font=('Courier', 12), bg='white', fg='black', width=25, command=self.generate_password)
        password_generator.pack()

    def generate_password(self):
        characters = string.ascii_letters + string.punctuation + string.digits
        password = "".join(choice(characters) for _ in range(28))
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)

# запуск застосунку
app = App()
app.window.mainloop()
