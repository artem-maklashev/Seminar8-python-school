import controller


def get_klass():
    klass = input('Введите наименование класса: (закончить -> 0) ').upper()
    if klass == '0':
        exit()
    else:
        return klass


def get_subject(data):
    print('\nПредметы\n')
    for i in range(len(data)):
        for key in data[i].keys():
            print(f'{i+1} {key}')
    user_input = get_number("\nВыберите предмет (выход -> 0): ", 0, len(data))
    return user_input-1


def show_students(subject_id):
    marks = ""
    subject = controller.data[subject_id]
    for key in subject.keys(): print(f'\n{key.title()}\n')
    for item in subject.values():
        for i in range(len(item)):
            for key, values in item[i].items():
                mark_list = [str(x) for x in values]
                marks = ", ".join(mark_list)
                print(f'{key:20}: {marks}')


def who_answers(subject_id):
    subject = controller.data[subject_id]
    is_correct = False
    while not is_correct:
        show_students(subject_id)
        name = input(
            '\nКто пойдет отвечать к доске? ("exit"- выбор предмета) ').title()
        for student in subject.values():           
            if name in student[0].keys() or name == 'Exit':                
                is_correct = True
            else:
                print('Такого ученика нет в этом классе')
    return name


def set_mark(student):
    if student != 'Exit':
        mark = get_number('Оцените знания ученика 1-5 :', 1, 5)
    else:
        return
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
