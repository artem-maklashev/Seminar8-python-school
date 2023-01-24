import controller

def get_klass():
    klass = input('Введите наименование класса: ').upper()
    return klass

def get_subject(data):
    for i in range(len(data)):
        for key in data[i].keys():
            print(f'{i+1} {key}')
    user_input = int(input("Выбеите предмет: "))
    return i-1

def show_students(subject_number):
    marks=""
    subject = controller.data[subject_number]
    for item in subject.values():
        for i in range(len(item)):
            for key, values in item[i].items():
                    mark_list = [str(x) for x in values]
                    marks = ", ".join(mark_list)
                    print(f'{key:20}: {marks}')
            

def who_answers(subject):
     students = controller.data[subject]
     name = input('Кто пойдет отвечать к доске? ')

    