import os

def rename_human_files(folder_path):
    """
    Переименовывает файлы из формата 'human1.json' в 'human.1.json'.

    :param folder_path: Путь к папке с файлами.
    """
    # Проверяем, существует ли папка
    if not os.path.isdir(folder_path):
        print(f"Папка не найдена: {folder_path}")
        return

    # Проходим по всем файлам в папке
    for filename in os.listdir(folder_path):
        # Проверяем, соответствует ли файл формату humanN.json
        if filename.startswith("human") and filename.endswith(".json"):
            try:
                # Разделяем имя файла на части (human + номер + .json)
                base, number = filename.split("human")
                number, ext = number.split(".json")

                # Формируем новое имя файла
                new_filename = f"human.{number}.json"
                old_filepath = os.path.join(folder_path, filename)
                new_filepath = os.path.join(folder_path, new_filename)

                # Переименовываем файл
                os.rename(old_filepath, new_filepath)
                print(f"Переименовано: {filename} -> {new_filename}")
            except ValueError:
                print(f"Файл пропущен: {filename} (не соответствует формату humanN.json)")
    print("Переименование завершено.")

# Пример использования
folder = "C:/Users/Сергей/AppData/Roaming/Blender Foundation/Blender/4.3/mpfb/config"  # Укажите путь к вашей папке
rename_human_files(folder)