import Note
import Unit_Interfase as ui
import File_operation
import time

def add():
    note = ui.create_note()
    array = File_operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    File_operation.write_file(array, 'a')
    time.sleep(1)
    print('Заметка добавлена...')

def show(text):
    logic = True
    array = File_operation.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки...')

def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = File_operation.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note()
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                time.sleep(1)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                time.sleep(1)
                print('Заметка удалена...')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    File_operation.write_file(array, 'a')
