import os

def list_male_skins(directory):
    # Проверяем, существует ли указанный путь
    if not os.path.isdir(directory):
        print(f"Указанный путь {directory} не существует.")
        return

    # Список для хранения найденных скинов
    male_skins = []

    # Проходимся по всем вложенным папкам
    for folder in os.listdir(directory):
        # Полный путь к папке
        folder_path = os.path.join(directory, folder)

        # Проверяем, что это папка и соответствует критериям
        if os.path.isdir(folder_path) and "male" in folder and "female" not in folder:
            male_skins.append(folder)

    # Выводим результат
    if male_skins:
        print("Найденные папки с 'male' (без 'female') в названии:")
        for skin in male_skins:
            print(skin)
    else:
        print("Папки с 'male' (без 'female') в названии не найдены.")

# Укажите путь к папке со скинами
skins_directory = "C:/Users/Сергей/AppData/Roaming/Blender Foundation/Blender/4.3/mpfb/data/skins"  # Замените на ваш путь
list_male_skins(skins_directory)