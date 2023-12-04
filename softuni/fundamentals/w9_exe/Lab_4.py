students = []
course = None

while True:
    student_info = input()

    if ":" not in student_info:
        course = student_info
        break

    name, ID, course = student_info.split(":")
    students.append({'name': name, "ID": ID, "course": course})

for i in students:
    if course in i.values():
# if course.startswith(i["course"][0:5]): #check whether the first five letters of the course each student "i" is taking with the provided course in the end
        print(f"{i['name']} - {i['ID']}")
