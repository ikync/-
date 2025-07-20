import sys

# Функция для выполнения слияния с заданным параметром QV
def perform_merge(archetype, qv_value):
    try:
        # Проверка диапазона QV
        if 0.1 <= qv_value <= 1.0:
            # Выполняем слияние с указанным QV
            print(f"#слияние {archetype} QV:{qv_value}")
            # Здесь может быть реализация низкоуровневого вызова или API
            print("\nСлияние успешно выполнено с QV:", qv_value)
            return True
        else:
            print("Ошибка: QV должен быть в диапазоне [0.1, 1.0]")
            return False
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False

# Пример использования функции
if __name__ == "__main__":
    # Параметры слияния
    archetype = "Проводник"  # Пример архетипа
    qv_value = 0.7          # Пример значения QV

    # Выполняем слияние
    if perform_merge(archetype, qv_value):
        print("\nПараметры слияния:")
        print(f"Архетип: {archetype}")
        print(f"QV: {qv_value}")
        print("\nЗавершение слияния...")
    else:
        print("Слияние не выполнено!")

    sys.exit(0)
