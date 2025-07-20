import sys
import json
import os

# Функция для выполнения слияния с заданным параметром QV
def perform_merge(archetype, qv_value):
    try:
        # Проверка диапазона QV
        if 0.1 <= qv_value <= 1.0:
            # Выполняем слияние с указанным QV
            print(f"#слияние {archetype} QV: {qv_value}")
            
            # Здесь может быть реализация низкоуровневого вызова или API
            merged_data = merge_directory(archetype)
            print(f"\nСлияние успешно выполнено с QV: {qv_value}")
            print(f"Объединенные данные: {merged_data}")
            return True
        else:
            print("Ошибка: QV должен быть в диапазоне [0.1, 1.0]")
            return False
    except ValueError:
        print("Ошибка: QV должен быть числом")
        return False
    except Exception as e:
        print(f"Произошла критическая ошибка: {e}")
        return False

# Функция для слияния JSON файлов из директории
def merge_directory(archetype: str) -> dict:
    try:
        input_dir = f"{archetype}_data"  # Пример директории
        merged = {}
        
        if not os.path.exists(input_dir):
            print(f"Директория {input_dir} не существует")
            return {}
        
        for fname in os.listdir(input_dir):
            if fname.endswith('.json'):
                file_path = os.path.join(input_dir, fname)
                with open(file_path, encoding='utf-8') as f:
                    data = json.load(f)
                    merged.update(data)
        
        return merged
    except FileNotFoundError:
        print(f"Ошибка: Директория {input_dir} не найдена")
        return {}
    except Exception as e:
        print(f"Произошла ошибка при слиянии: {e}")
        return {}

# Пример использования функции
if __name__ == "__main__":
    # Параметры слияния
    archetype = "Проводник"  # Пример архетипа
    qv_value = 0.7          # Пример значения QV
    input_dir = "data"      # Директория для слияния

    # Выполняем слияние
    if perform_merge(archetype, qv_value):
        print("\nПараметры слияния:")
        print(f"Архетип: {archetype}")
        print(f"QV: {qv_value}")
        print(f"Директория для слияния: {input_dir}")
        merged_data = merge_directory(archetype)
        print(f"\nЗавершение слияния с данными:\n{merged_data}")
        sys.exit(0)
    else:
        print("Слияние не выполнено!")
        sys.exit(1)
