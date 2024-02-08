from database import DatabaseManager


class SearchManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager


    def search_notes(self, keyword) -> str:
        return self.db_manager.search_notes(keyword)


if __name__ == "__main__":
    db_manager = DatabaseManager()
    search_manager = SearchManager(db_manager)

    keyword = input("Введите ключевое слово для поиска заметок: ")
    matching_notes = search_manager.search_notes(keyword)

    if matching_notes:
        print("Результаты поиска:")
        for note in matching_notes:
            print(f"Заметка ID: {note[0]}, Заголовок: {note[1]}")
    else:
        print("По вашему запросу ничего не найдено.")
