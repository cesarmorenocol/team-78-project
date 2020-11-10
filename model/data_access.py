import pandas as pd

class DataAccess():

    df_hour = pd.read_csv(r'model/data/df_group_hora.csv', encoding='utf_8',delimiter=';')
    df_day = pd.read_csv(r'model/data/df_group_dia.csv', encoding='utf_8',delimiter=';')
    df_date = pd.read_csv(r'model/data/df_group_fecha.csv', encoding='utf_8',delimiter=';')
    dfp = pd.read_csv('model/data/df_lineasFecha.csv', dtype='unicode', encoding='utf_8',decimal='.')