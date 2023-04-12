import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 487727948 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    flag = True
    if ttest_ind(x, y, equal_var=False, alternative="less").pvalue >= 0.01:
        flag = False
    return flag # Ваш ответ, True или Fals
