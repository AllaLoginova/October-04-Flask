import tkinter as tk
from abc import ABC, abstractmethod
import json


class NoteModel:
    """База данных для хранения заметок"""
    def __init__(self):
        self._notes = self._load_from_file()

    def get_notes(self):
        return self._notes

    def add_note(self, text):
        next_id = self._get_last_id() + 1 # получаем новый id
        note = {"id": next_id, "text": text} # создаем заметку
        self._notes.append(note) # добавляем в список
        self.save_to_file()

    def delete_by_id(self, note_id):
        for number, note in enumerate(self._notes):
            if note['id'] == note_id:
                self._notes.pop(number)
                break
        else:
            print('Такой заметки нет')

    def find_by_text(self, text_to_find):
        res = []
        for note in self._notes:
            if text_to_find in note['text']:
                res.append(note)
        return res


    def _load_from_file(self):
        """Загрузка данных из файла"""
        with open('notes.json', 'r', encoding='utf-8') as f:
            notes = json.load(f)
        return notes

    def save_to_file(self):
        with open('notes.json', 'w', encoding='utf-8') as f:
            notes = json.dump(self._notes, f)
        return notes

    def _get_last_id(self):
        """ """
        if self._notes:
            max = self._notes[0]['id']
            for note in self._notes:
                if note['id'] > max:
                    max = note['id']
        else:
            max = 0

        return max

class AbstractView(ABC):
    @abstractmethod
    def render_notes(self, notes):
        pass

class GrafocView(AbstractView):
    # def __init__(self):
    #     self.root = tk.Tk()
    #     self.root.title('Тестовое окошко')
    #     self.listbox = tk.Listbox(self.root, height=10, width=50)
    #     self.listbox.pack(padx=10, pady=10)

    def render_notes(self, notes):
        self.create_window()
        for note in notes:
            text = f"{note['id']} --- {note['text']}"
            self.listbox.insert(tk.END, text)
        self.root.mainloop()

    def create_window(self):
        self.root = tk.Tk()
        self.root.title('Тестовое окошко')
        self.listbox = tk.Listbox(self.root, height=10, width=50)
        self.listbox.pack(padx=10, pady=10)

class ConsoleViewe(AbstractView):
    def render_notes(self, notes):
        for note in notes:
            text = f"{note['id']} --- {note['text']}"
            print(text)

    @staticmethod
    def find_by_text(lst):
        print(*lst)


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_notes(self):
        """ Покзать все заметки"""
        notes = self.model.get_notes()
        self.view.render_notes(notes)
        # for note in notes:
        #     print(f"{note['id']} - {note['text']}")

    def add_note(self):
        text = input('Введи текст заметки ')
        self.model.add_note(text)

    def delete_note(self):
        self.show_notes()
        note_id = int(input('Введи id заметки'))
        self.model.delete_by_id(note_id)

    def find_by_text(self):
        text_to_find = input('Введи текст ')
        lst = self.model.find_by_text(text_to_find)
        self.view.render_notes(lst)

model = NoteModel()
grafic_view = GrafocView()
consol_view = ConsoleViewe()
contr = Controller(model, consol_view)



while True:
    print("1 - посмотреть все заметки")
    print('2 - Добавить заметку')
    print('3 - Удалить заметку')
    print('4 - Найти заметки с текстом ')
    print("q - Выйти")

    choice = input("Выбирай: ")
    if choice == '1':
        contr.show_notes()
    elif choice == '2':
        contr.add_note()
    elif choice == '3':
        contr.delete_note()
    elif choice == '4':
        contr.find_by_text()
    elif choice == 'q':
        break

