student_data = {}

print('\nSTUDENT DATABASE')

for i in range(10):
    student_number = int(input('\nPlease, enter your ID number: '))
    student_data[student_number] = int(input('Please, enter your height (in centimeters): '))

tallest_student = max(student_data, key=student_data.get)
shortest_student = min(student_data, key=student_data.get)

print(f"\nThe tallest student is the student {tallest_student} and his height is "
      f"{student_data[tallest_student]}. "
      f"The shortest student is the student {shortest_student} and his height is "
      f"{student_data[shortest_student]}.")
