import module
import view



def start():
    
    global data
    
    while True:
        class_selection = view.get_klass()
        
        data = module.read_file(class_selection)
        subject = view.get_subject(data)
        view.show_students(subject)

