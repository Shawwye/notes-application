from database import DatabaseManager


class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content


# класс для управления заметками
class NotesManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager


    def add_note(self, title, content):
        note = Note(title, content)
        self.db_manager.add_note(note.title, note.content)


    def get_all_notes(self):
        return self.db_manager.get_all_notes()


    def get_note_by_id(self, note_id):
        return self.db_manager.get_note_by_id(note_id)


    def search_notes(self, keyword):
        return self.db_manager.search_notes(keyword)


    def delete_note_by_id(self, note_id):
        self.db_manager.delete_note_by_id(note_id)
