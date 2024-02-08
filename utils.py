import re


def validate_input(text, max_length) -> bool:
    """
    проверяет, что введенный текст не пустой и не превышает максимальную длину.

    :param text: Введенный текст
    :param max_length: Максимальная длина текста
    :return: True, если текст валиден, иначе False
    """
    if not text:
        print("Ошибка: Введите текст.")
        return False
    
    if len(text) > max_length:
        print(f"Ошибка: Текст не должен превышать {max_length} символов.")
        return False
    
    return True


def sanitize_input(text) -> str:
    """
    очищает введенный текст от опасных символов.

    :param text: Введенный текст
    :return: Очищенный текст
    """
    sanitized_text = re.sub(r'[;\'"<>]', '', text)
    
    return sanitized_text
