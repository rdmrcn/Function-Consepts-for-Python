
#print(hello_func('Hi', name = 'Reha))
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math','Arth  ']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)
