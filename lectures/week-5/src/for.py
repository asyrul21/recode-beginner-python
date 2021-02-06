students = [ "Ali", "Abu", "John", "Siti", "Bob" ]

print("The For In Loop")
print("Print Students who name starts with an A:")
for student in students:
    if student[0] == "A" or student[0] == "a":
        print(student)
    
print()
print("The For in Enumerate Loop")
for index, student in enumerate(students):
    print("Index: " + str(index) + " Name: " + student)

print()
print("Print Only Student at 2nd and 3rd Position:")
for index, student in enumerate(students):
    if(index == 1 or index == 2):
        print(student)