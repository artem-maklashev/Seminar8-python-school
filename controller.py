import module
import view


#global subject

def start():
    
    while True:
        class_selection = view.get_klass()
        global data
        data = module.read_file(class_selection)
        subject = view.get_subject(data)
        view.show_students(subject)
        study(subject)
        
def study(index):
    student = view.who_answers(index)
    mark = view.set_mark()
    module.save_mark(mark, student, index)

