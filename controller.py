import model
import view

def start():
    
    while True:
        global selection_class
        global data
        selection_class = view.get_klass()        
        data = model.read_file(selection_class)
        is_exit = False
        while not is_exit:
            is_exit = subject_selection()
        
def subject_selection():
    
    subject = view.get_subject(data)
    while subject != -1:
        study(subject)
        subject = view.get_subject(data)
    return True

def study(index):
    student = ""
    while student != 'Exit':
        student = view.who_answers(index)
        mark = view.set_mark(student)
        model.save_mark(mark, student, index)
        model.save_file(selection_class)
    

