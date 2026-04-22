python_students={"Aradhya","Anamika","Arushi","Noah","Mick"}
data_students={"Noah","Ben","Max","Mick","Anamika","Millie","Adhithi"}
print("->Total number of students enrolled in Python:",len(python_students))
print("->Total number of students enrolled in Data:",len(data_students))
print("->Students enrolled in both courses:",python_students.intersection(data_students))
print("Students enrolled in only Python:",python_students.difference(data_students))
print("->Students enrolled in only Data Professional Trainee:",data_students.difference(python_students))
print("->All unique students enrolled:\n",python_students.union(data_students))
students_info={
    "Aradhya":{"age":19,"course":"Python"},
    "Anamika":{"age":18,"course":"Both"},
    "Arushi":{"age":20,"course":"Python"},
    "Noah":{"age":22,"course":"Both"},
    "Mick":{"age":23,"course":"Both"},
    "Ben":{"age":20,"course":"Data"},
    "Max":{"age":21,"course":"Data"},
    "Millie":{"age":22,"course":"Data"},
    "Adhithi":{"age":20,"course":"Data"}
}
print("->All student names:")
for name in students_info:print(name,end=" ")
print("\n->Each student’s name with age and course:")
for name,details in students_info.items():
    print(name,"-","Age:",details["age"],"Course:",details["course"])
students_info["Noah"]["course"]="Python"
print("->Course of Noah updated from \"Both\" to \"Python\":",students_info["Noah"])
del students_info['Arushi']
print("->Student info of Arushi deleted")