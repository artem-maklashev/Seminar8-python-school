import json


def read_file(file):
    file_name = file +'.json'
    try:
        with open(file_name, 'r', encoding='utf-8') as data_file:
            data_from_db =  json.load(data_file)
    except:
        print('Файл не существует.')
    return data_from_db
