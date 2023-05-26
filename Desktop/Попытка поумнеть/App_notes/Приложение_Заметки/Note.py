from datetime import datetime
import uuid

class Note:
    def __init__(self, id =str(uuid.uuid1())[0:2], 
                title= "text",
                body = "text", 
                date = str(datetime.now().strftime("%d.%m.%Y %H:%M"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def get_id(note):
        return note.id
    
    def get_title(note):
        return note.title
    
    def get_body(note):
        return note.body
    
    def get_date(note):
        return note.date
    
    def set_id(note):
        note.id = str(uuid.uuid1())[0:2]

    def set_title(note, title):
        note.title = title
    
    def set_body(note, body):
        note.body = body

    def set_date(note):
        str(datetime.now().strftime("%d.%m.%Y %H:%M "))

    
    def to_string(note):
        return note.id + ";" + note.title + ";" + note.body + ";" + note.date
    
    def map_note(note):
        return '\nid:' + note.id + '\n' + 'Название: ' + note.title + '\n' + 'Описание: ' + note.body + '\n' + 'Дата создания: ' + note.date
        