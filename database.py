import sqlite3


class DatabaseManager:
    def __init__(self, db_name='notes.db'):
        self.db_name = db_name
        self.conn = None
        self.cursor = None


    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()


    def disconnect(self):
        if self.conn:
            self.conn.close()


    def create_table(self):
        self.connect()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                title TEXT,
                content TEXT
            )
        ''')
        self.conn.commit()
        self.disconnect()


    def add_note(self, title, content):
        self.connect()

        self.cursor.execute('SELECT id FROM notes WHERE title = ?', (title,))
        existing_note = self.cursor.fetchone()

        if existing_note:
            print("Заметка с таким заголовком уже существует.")
        else:
            self.cursor.execute('''
                INSERT INTO notes (title, content)
                VALUES (?, ?)
            ''', (title, content))
            self.conn.commit()
            print("Заметка успешно добавлена.")

        self.disconnect()

    def get_all_notes(self) -> str:
        self.connect()
        
        self.cursor.execute('SELECT id, title FROM notes')
        notes = self.cursor.fetchall()
        
        self.disconnect()
        
        return notes


    def get_note_by_id(self, note_id):
        self.connect()
        self.cursor.execute('SELECT * FROM notes WHERE id = ?', (note_id,))
        note = self.cursor.fetchone()
        self.disconnect()
        return note


    def search_notes(self, keyword) -> str:
        self.connect()
        self.cursor.execute('SELECT id, title FROM notes WHERE content LIKE ? OR title LIKE ?',
                            (f'%{keyword}%', f'%{keyword}%'))
        matching_notes = self.cursor.fetchall()
        self.disconnect()
        
        return matching_notes


    def delete_note_by_id(self, note_id):
        self.connect()

        self.cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
        
        self.conn.commit()
        self.disconnect()
