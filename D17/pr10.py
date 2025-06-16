import uuid

students = ["student1", "student2", "student3"]
student_ids = {}

for student in students:
    student_ids[student] = str(uuid.uuid4())

print("Student UUIDs:")
for name, uid in student_ids.items():
    print(name, ":", uid)
