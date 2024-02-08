from database import DatabaseManager
from notes import NotesManager
from search import SearchManager
from utils import validate_input, sanitize_input


def display_menu() -> None:
    print("\nМенеджер заметок")
    print("1. Просмотреть список заметок")
    print("2. Добавить новую заметку")
    print("3. Поиск заметок")
    print("4. Удалить заметку")
    print("5. Просмотреть заметку по ID")
    print("6. Выйти")


def main():
    db_manager = DatabaseManager()
    db_manager.create_table()

    notes_manager = NotesManager(db_manager)
    search_manager = SearchManager(db_manager)

    while True:
        display_menu()
        choice = input("Выберите опцию: ")

        if choice == "1":
            notes = notes_manager.get_all_notes()
            if notes:
                print("\nСписок заметок:")
                for note in notes:
                    print(f"Заголовок: {note[1]} (ID: {note[0]})")
            else:
                print("Список заметок пуст.")

        elif choice == "2":
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержание заметки: ")

            if validate_input(title, 255) and validate_input(content, 1000):
                title = sanitize_input(title)
                content = sanitize_input(content)
                notes_manager.add_note(title, content)

        elif choice == "3":
            keyword = input("Введите ключевое слово для поиска: ")
            matching_notes = search_manager.search_notes(keyword)

            if matching_notes:
                print("\nРезультаты поиска:")
                for note in matching_notes:
                    print(f"Заголовок: {note[1]} (ID: {note[0]})")
            else:
                print("По вашему запросу ничего не найдено.")

        elif choice == "4":
            note_id = input("Введите ID заметки, которую вы хотите удалить: ")
            if note_id.isdigit():
                note_id = int(note_id)
                notes_manager.delete_note_by_id(note_id)
                print(f"Заметка с ID {note_id} удалена.")
            else:
                print("Некорректный ID заметки. Введите число.")

        elif choice == "5":
            note_id = input("Введите ID заметки для просмотра: ")
            if note_id.isdigit():
                note_id = int(note_id)
                note = notes_manager.get_note_by_id(note_id)
                if note:
                    print(f"\n\nЗаголовок: {note[1]}")
                    print(f"Содержание:\n{note[2]}")
                else:
                    print(f"Заметка с ID {note_id} не найдена.")
            else:
                print("Некорректный ID заметки. Введите число.")

        elif choice == "6":
            print("Выход из приложения.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, выберите опцию из меню.")


if __name__ == "__main__":
    main()
