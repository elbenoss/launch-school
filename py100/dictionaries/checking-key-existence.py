#Check whether the keys 'name' and 'grade' exist in the following dictionary:

student = {
    'id': 123,
    'grade': 'B',
}

print('name' in student)
print('grade' in student)
print(student.get('name') is not None)
print(student.get('grade') is not None)