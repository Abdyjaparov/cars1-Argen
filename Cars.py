import os
import shutil

# Функция для создания новой папки, выбора существующей или удаления папки для бренда автомобиля
def select_or_create_folder():
    while True:
        print("\n--- Выберите, создайте или удалите папку бренда автомобиля ---")
        print("1. Создать новую папку")
        print("2. Использовать существующую папку")
        print("3. Удалить папку")
        choice = input("Введите ваш выбор: ")
        
        if choice == '1':
            # Создать новую папку
            while True:
                folder_name = input("Введите НОВОЕ имя папки для хранения информации об автомобиле: ")
                if os.path.exists(folder_name):
                    print("Неверный ввод: Папка уже существует. Пожалуйста, выберите другое имя.")
                else:
                    os.makedirs(folder_name)
                    print(f"Папка '{folder_name}' создана.")
                    return folder_name
        
        elif choice == '2':
            # Использовать существующую папку
            folders = [f for f in os.listdir() if os.path.isdir(f)]
            if not folders:
                print("Нет доступных существующих папок. Пожалуйста, создайте новую папку.")
                continue

            print("\nДоступные папки брендов автомобилей:")
            for i, folder in enumerate(folders, start=1):
                print(f"{i}. {folder}")
            
            try:
                folder_choice = int(input("Введите номер папки, которую хотите использовать: ")) - 1
                if 0 <= folder_choice < len(folders):
                    return folders[folder_choice]
                else:
                    print("Неверный выбор. Пожалуйста, попробуйте снова.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите число.")
        
        elif choice == '3':
            # Удалить существующую папку
            folders = [f for f in os.listdir() if os.path.isdir(f)]
            if not folders:
                print("Нет доступных папок для удаления.")
                continue

            print("\nДоступные папки для удаления:")
            for i, folder in enumerate(folders, start=1):
                print(f"{i}. {folder}")
            
            try:
                folder_choice = int(input("Введите номер папки, которую хотите удалить: ")) - 1
                if 0 <= folder_choice < len(folders):
                    folder_to_delete = folders[folder_choice]
                    confirmation = input(f"Вы уверены, что хотите удалить папку '{folder_to_delete}'? (да/нет): ").lower()
                    if confirmation == 'да':
                        shutil.rmtree(folder_to_delete)
                        print(f"Папка '{folder_to_delete}' была удалена.")
                    else:
                        print("Удаление отменено.")
                else:
                    print("Неверный выбор. Пожалуйста, попробуйте снова.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите число.")
        
        else:
            print("Неверный выбор. Введите 1, 2 или 3.")

# Функция для проверки уникальности ID автомобиля и его сохранения
def check_and_save_car_id():
    while True:
        print("\n--- Введите ID автомобиля ---")
        car_id = input("Введите уникальный ID автомобиля: ")
        with open("CarsID.txt", "a+") as f:
            f.seek(0)
            existing_ids = f.read().splitlines()
            if car_id in existing_ids:
                print("Неверный ввод: Этот ID автомобиля уже существует. Пожалуйста, используйте уникальный ID.")
            else:
                f.write(car_id + "\n")
                return car_id

# Функция для сохранения информации об автомобиле в указанной папке
def save_car_info(folder_name, car_id, car_info):
    file_path = os.path.join(folder_name, f"{car_id}.txt")
    with open(file_path, "w") as car_file:
        car_file.write(car_info)
    print(f"\nИнформация об автомобиле сохранена в '{file_path}'\n")

# Функция для просмотра существующих папок и файлов автомобилей в них
def view_cars():
    print("\n--- Просмотр существующих брендов автомобилей ---")
    folders = [f for f in os.listdir() if os.path.isdir(f)]
    if not folders:
        print("Нет доступных брендов автомобилей.")
        return
    
    print("\nДоступные бренды автомобилей:")
    for i, folder in enumerate(folders, start=1):
        print(f"{i}. {folder}")
    
    try:
        folder_choice = int(input("\nВведите номер бренда, который хотите просмотреть: ")) - 1
        if 0 <= folder_choice < len(folders):
            selected_folder = folders[folder_choice]
            files = [f for f in os.listdir(selected_folder) if f.endswith('.txt')]
            if not files:
                print(f"\nНет автомобилей в бренде '{selected_folder}'.")
                return
            
            print(f"\nДоступные автомобили в бренде '{selected_folder}':")
            for i, file in enumerate(files, start=1):
                print(f"{i}. {file}")
            
            file_choice = int(input("\nВведите номер автомобиля, который хотите просмотреть: ")) - 1
            if 0 <= file_choice < len(files):
                selected_file = files[file_choice]
                with open(os.path.join(selected_folder, selected_file), "r") as f:
                    print("\n--- Информация об автомобиле ---")
                    print(f.read())
            else:
                print("Неверный выбор.")
        else:
            print("Неверный выбор.")
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число.")

# Основная функция для отображения меню
def main():
    print("Добро пожаловать в приложение Car Dealer")

    while True:
        print("\n--- Главное меню ---")
        print("1. Добавить новый автомобиль")
        print("2. Просмотреть существующие автомобили")
        print("3. Выйти")
        choice = input("Введите ваш выбор: ")
        
        if choice == '1':
            # Выбрать или создать папку и сохранить новую информацию об автомобиле
            folder_name = select_or_create_folder()
            car_id = check_and_save_car_id()
            
            print("\n--- Введите данные автомобиля ---")
            car_model = input("Введите модель автомобиля: ")
            car_year = input("Введите год выпуска: ")
            car_price = input("Введите цену автомобиля: ")
            car_color = input("Введите цвет автомобиля: ")

            car_info = f"Car ID: {car_id}\nМодель: {car_model}\nГод выпуска: {car_year}\nЦена: {car_price}\nЦвет: {car_color}\n"
            save_car_info(folder_name, car_id, car_info)
        
        elif choice == '2':
            view_cars()
        
        elif choice == '3':
            print("\nВыход из приложения. До свидания!")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, введите число из предложенных вариантов меню.")

if __name__ == "__main__":
    main()
