import os
import multiprocessing

# Функция для генерации чисел с плавающей точкой в диапазоне
def frange(start, stop, step):
    while start < stop:
        yield round(start, 10)  # Округление для избежания ошибок точности
        start += step

# Параметры изменения значений
fixed_age = 0.33
#muscle_values = [round(x, 2) for x in frange(0.1, 1.06, 0.06)]  # 16 значений
weight_values = [round(x, 2) for x in frange(0.25, 1.05, 0.05)]  # 16 значений
height_values = [round(x, 3) for x in frange(0.55, 0.774, 0.014)]  # 16 значений

# Значения Muscle, которые нужно дополнить
muscle_to_add = [0.1, 0.4, 0.7, 1.0]

# Путь для сохранения файлов
output_dir = "/home/samvel/Desktop/Database3/mhm1024added"
os.makedirs(output_dir, exist_ok=True)

# Функция для создания одного файла
def create_file(params):
    muscle, weight, height, file_counter = params

    filename = f"male_{file_counter}.mhm"
    filepath = os.path.join(output_dir, filename)

    content = f"""
# Written by MakeHuman 1.2.0 final
version v1.2.0
camera 0.0 0.0 0.0 0.0 0.0 1.0
modifier breast/BreastSize 0.500000
modifier breast/BreastFirmness 0.500000
modifier macrodetails/Gender 1.000000
modifier macrodetails/Age {fixed_age}
modifier macrodetails/African 0.333333
modifier macrodetails/Asian 0.333333
modifier macrodetails/Caucasian 0.333333
modifier macrodetails-universal/Muscle {muscle}
modifier macrodetails-universal/Weight {weight}
modifier macrodetails-height/Height {height}
modifier macrodetails-proportions/BodyProportions 0.500000
eyes HighPolyEyes 2c12f43b-1303-432c-b7ce-d78346baf2e6
clothesHideFaces True
skinMaterial skins/default.mhmat
material HighPolyEyes 2c12f43b-1303-432c-b7ce-d78346baf2e6 eyes/materials/brown.mhmat
subdivide True
"""
    # Запись в файл
    with open(filepath, "w") as file:
        file.write(content.strip())

# Создание параметров для параллельного выполнения
params_list = []
file_counter = 4097
for height in height_values:
    for weight in weight_values:
        for muscle in muscle_to_add:
            params_list.append((muscle, weight, height, file_counter))
            file_counter += 1

# Используем multiprocessing для ускорения
if __name__ == "__main__":
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(create_file, params_list)

# Мощность базы данных
power = len(height_values) * len(weight_values) * len(muscle_to_add)
if __name__ == "__main__":
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(create_file, params_list)
    
    print(f"Всего файлов: {len(params_list)}")
    print(f"Мощность базы данных: {power}")
