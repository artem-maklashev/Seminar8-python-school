import json
import controller


def read_file(file):
    file_name = file +'.json'
    try:
        with open(file_name, 'r', encoding='utf-8') as data_file:
            data_from_db =  json.load(data_file)
    except:
        print('Файл не существует.')
    return data_from_db

def save_mark(mark, student, index):
    subject = controller.data[index]
    for students in subject.values():
        for student_, marks in students[0].items():
            if student_ == student:
                marks.append(mark)

    print(subject)
