import time


def sleep_one_sec():
    # Запоминаем время перед выполнением исходной функции.
    start_time = time.time()
    # Выполняем код исходной функции:
    time.sleep(1)
    # Вычисляем, округляем и печатаем разницу
    # между временем старта и актуальным временем.
    execution_time = round(time.time() - start_time, 1)
    print(f'Время выполнения функции: {execution_time} сек.')
    return 'Результат первой функции.'


def sleep_two_sec():
    start_time = time.time()
    # Теперь выполняем код исходной функции:
    time.sleep(2)
    execution_time = round(time.time() - start_time, 1)
    print(f'Время выполнения функции: {execution_time} сек.')
    return 'Результат второй функции.' 