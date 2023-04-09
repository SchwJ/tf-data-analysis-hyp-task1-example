import pandas as pd
import numpy as np


chat_id = 5191217616 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return proportions_ztest([y_success, x_success], [y_cnt, x_cnt], alternative="larger")[1] < 0.03 # Ваш ответ, True или False
