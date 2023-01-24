import controller


def get_klass():
    klass = input('Введите наименование класса: ').upper()
    return klass


def get_subject(data):
    for i in range(len(data)):
        for key in data[i].keys():
            print(f'{i+1} {key}')
    user_input = int(input("Выбеите предмет: "))
    return user_input-1


def show_students(subject_number):
    marks = ""
    subject = controller.data[subject_number]
    for item in subject.values():
        for i in range(len(item)):
            for key, values in item[i].items():
                    mark_list = [str(x) for x in values]
                    marks = ", ".join(mark_list)
                    print(f'{key:20}: {marks}')


def who_answers(subject_id):
     subject = controller.data[subject_id]
     print(subject)
     is_correct = False
     while not is_correct:
        name = input(
            'Кто пойдет отвечать к доске? ("exit"- в основное меню) ').title()
        for student in subject.values():
            print(student[0])
            for key in student[0].keys():
                print(f'key {key} --> name {name}')
                if key == name or name == 'Exit':
                    is_correct = True
            else:
                print('Такого ученика нет в этом классе')
     if name == 'exit':
        return
     else:
         return name
     
def set_mark():
    mark = get_number('Оцените знания ученика 1-5', 1, 5)
    return mark


def get_number(message, min_number=0, max_number=1):
    isCorrect = False
    while isCorrect == False:
        try:
            number = int(input(message))
            if number in range(min_number, max_number+1):
                isCorrect = True
            else:
                print(f'Значение должно быть от {min_number} до {max_number}')
        except ValueError:
            print("Введено не целое число. Повторите ввод ")
    return number



    