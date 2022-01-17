student_data = {}

print('\nSTUDENT DATABASE')

for i in range(10):
    student_number = int(input('\nPlease, enter your ID number: '))
    student_data[student_number] = int(input('Please, enter your height (in centimeters): '))

max_height = max(student_data, key=student_data.get)
min_height = min(student_data, key=student_data.get)

print(f"\nThe tallest student is the student {max_height} and his height is "
      f"{student_data[max_height]}. "
      f"The shortest student is the student {min_height} and his height is "
      f"{student_data[min_height]}.")
