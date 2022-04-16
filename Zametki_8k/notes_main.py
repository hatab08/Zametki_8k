#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication , QWidget , QPushButton , QHBoxLayout , QVBoxLayout , QLabel , QMessageBox , QRadioButton , QGroupBox , QButtonGroup, QListWidget, QLineEdit, QTextEdit, QInputDialog
import json


app = QApplication([])
notes = {"Добро Пожаловать":{
    "текст":"Здесь нужно написать что-то",
    "теги":["Добро", "Начало работы"]}
}
with open ("notes_data.json", "w") as file:
    json.dump(notes,file)
notes_win = QWidget()
notes_win.setWindowTitle("Заметки в 8K разрешении. Создатель: Миша#228")
notes_win.resize(7680,4320)
list_notes = QListWidget()
list_notes_label = QLabel("Список Заметок")
button_note_create = QPushButton("Создать заметку")
button_note_del = QPushButton("Анигилировать заметку")
button_note_save = QPushButton("Сохранить заметку")
field_text = QTextEdit()
field_tag = QLineEdit("")
field_tag.setPlaceholderText("Введите тег........")
button_tag_add = QPushButton("Добавить к заметке")
button_tag_del = QPushButton("Открепить от заметки")
button_search = QPushButton("Искать заметку")
list_tags = QListWidget()
list_tag_label = QLabel('Список тегов')


layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)
col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2) 
col_2.addWidget(list_tag_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)

row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_search)
col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1)
layout_notes.addLayout(col_2)
notes_win.setLayout(layout_notes)
def show_note():
    name = list_notes.selectedItems()[0].text()
    field_text.setText(notes[name]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[name]["теги"])
def add_note():
    note_name, ok = QInputDialog.getText(
        notes_win, "Добавить Заметку", "Название Заметки:"   
    )
    if ok and note_name != "":
        notes[note_name] = {"Текст" : "", "теги" : []}
        list_notes.addItem(note_name)
button_note_create.clicked.connect(add_note)        
    
def del_note():
    key = list_notes.selectedItems()[0].text()
    del notes[key]
    with open('notes.json',"w") as file:
        json.dump(notes,file)
    list_notes.clear()
    list_tags.clear()
    field_text.clear()
    list_notes.addItems(notes)

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['текст'] = field_text.toPlainText()
        with open('notes_data.json',"w") as file:
            json.dump(notes,file, sort_keys = True)
button_note_save.clicked.connect(save_note)
button_note_del.clicked.connect(del_note)


def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys= True)
    else:
        print("Заметка Для добваления тега не выбрана!")
def del_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]["теги"])
        with open ("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys= True)

    else:
        print("Тег для удаления не выбран ЧМО!!!")  
def search_tag():
    tag = field_tag.text()
    if button_tag_search.text() == "Искать Заметки по тегу" and tag:
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]["теги"]:
                notes_filtered[note]=notes[note]
        button_tag_search.setText("Сбросить поиск")
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
    elif button_tag_search.text() == "Сбросить Поиск":
        field_tag.clear()
        list_notes.clear()
        list_tag.clear()
        list_notes.addItems(notes)
        button_tag_search.setText("искать Заметки по тегу")
    else:
        pass
                

button_tag_add.clicked.connect(add_tag)
button_tag_del.clicked.connect(del_tag)


    

notes_win.show()
app.exec_()











                                      













































    






  
























 




































 




































































  