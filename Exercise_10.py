import random

exam_notes = []

for i in range(15):
    exam_notes.append(random.randrange(0, 11))

print(f'The generated notes were {exam_notes}.')
print(f'The grade point average is {(sum(exam_notes))/15}.')
