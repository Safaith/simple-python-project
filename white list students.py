blackList = ["susan", "mickale", "robert", "messi", "ronaldo"]
studentlist = []
whitelist = []
num_students = int(input("num of students: "))
for student in range(num_students):
    name = input("Enter student name:  ")
    studentlist.append(name)
for student in studentlist:
    if student not in blackList:
        whitelist.append(student)
print(whitelist)
