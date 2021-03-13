
#Working with Python Functions.
def first_function():
    print("our first python function")


first_function()

def calculate_students_marks(english, maths, swahili):
    marks = english+maths+ swahili
    return marks

print(calculate_students_marks(69,70,70))

def movement(movement_type):
    return  movement_type
print(movement("walking"))

def get_student_name(name ):
    statement = "my name is {name} "
    return statement


print(get_student_name("Jack"))

def students_details(name, age, **marks):
    return name,age,marks


print(students_details("Jack",19,english=80,maths=88,swahili=54))


def area_of_circle(radius):
    area = 3.412*radius*radius
    return f"the area is {area} "

print(area_of_circle(10))

