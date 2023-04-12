import pandas as pd
import numpy as np


chat_id = 487727948 # Ваш chat ID, не меняйте название переменной

def solution(data: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    # Выполняем односторонний t-тест
    t_statistic, p_value = ttest_1samp(data, 300)
    
    # Проверяем нулевую гипотезу на заданном уровне значимости
    alpha = 0.1
    if p_value/2 < alpha and t_statistic < 0:
        return True # Отклоняем нулевую гипотезу
    else:
        return False # Не отклоняем нулевую гипотезу
