import pandas as pd
from global_data import GlobalData


# print(GlobalData.data_train)


df = pd.read_excel('D:\LSTM\sb_model_25_11_2023\data\HDM_test.xlsx')


#df = GlobalData.data_train
# Преобразуем столбец 'Дата' в формат даты
df['Дата'] = pd.to_datetime(df['Дата'], format='%m/%d/%Y')
# Находим максимальную дату
max_date = df['Дата'].max()
new_row = {'Дата': max_date + pd.DateOffset(months=1),
'Суммарная Qн, т/сут': 1,
'Суммарная Qж, м3/сут': 1}
df = df.append(new_row, ignore_index=True)
print(df)