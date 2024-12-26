import os
import shutil

def copy_missing_mhm_files(dir1, dir2, dir3):
    """
    Копирует mhm файлы из dir2 в dir3, если их имена не встречаются в dir1.

    Args:
        dir1: Путь к директории с названиями директорий (male_num).
        dir2: Путь к директории с mhm файлами.
        dir3: Путь к директории для копирования недостающих файлов.
    """
    # Получаем список названий директорий из dir1
    dir1_names = [name for name in os.listdir(dir1) if os.path.isdir(os.path.join(dir1, name))]
    # Получаем список имен mhm файлов из dir2
    dir2_names = [name.split('.')[0] for name in os.listdir(dir2) if name.endswith('.mhm')]
    # Находим недостающие файлы
    missing_files = [name for name in dir2_names if name not in dir1_names]
    # Копируем недостающие файлы в dir3
    for file_name in missing_files:
        source_path = os.path.join(dir2, file_name + '.mhm')
        destination_path = os.path.join(dir3, file_name + '.mhm')
        shutil.copy(source_path, destination_path)
    print(f"Скопировано {len(missing_files)} файлов в {dir3}")

# Пример использования
dir1 = 'C:\\Users\\HP 845 G8\\Desktop\\models\\Database3\\models'  # Путь к директории с названиями директорий
dir2 = 'C:\\Users\\HP 845 G8\\Desktop\\models\\Database3\\mhm'  # Путь к директории с mhm файлами
dir3 = 'C:\\Users\\HP 845 G8\\Desktop\\models\\Database3\\test'  # Путь к директории для копирования

copy_missing_mhm_files(dir1, dir2, dir3)