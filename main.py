import pandas as pd
import itertools

# Mavjud talabalar ro'yxati
talabalar = [
    {"ism": "Ali", "baholar": 85},
    {"ism": "Vali", "baholar": 90},
    {"ism": "Hasan", "baholar": 78},
    {"ism": "Husan", "baholar": 92},
    {"ism": "Tohir", "baholar": 88},
    {"ism": "Nuriddin", "baholar": 76},
    {"ism": "Abdulloh", "baholar": 95},
    {"ism": "Shohruh", "baholar": 89},
    {"ism": "Sobir", "baholar": 91},
    {"ism": "Rustam", "baholar": 80}
]

# Pandas DataFrame yaratish
df = pd.DataFrame(talabalar)

# Baholar bo'yicha guruhlash
guruhlar = itertools.groupby(sorted(df, key=lambda x: x['baholar']), key=lambda x: x['baholar'])

# Guruhlar uchun baholar va talabalar sonini chiqarish
for baholar, guruh in guruhlar:
    print(f"Baholar: {baholar}, Talabalar soni: {len(list(guruh))}")
