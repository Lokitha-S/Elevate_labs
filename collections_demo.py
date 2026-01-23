#list
students = ['Ramya', 'Vinoth', 'Sandhya', 'Vinusha', 'Vinusha', 'Vinusha']
students1 = ['Ram', 'Vinoth', 'Sandy', 'Vinusha', 'Kamal']
students.append("Raghu")
students.remove('Ramya')
students.sort()             


#tuple
fun_tuple=("Rajesh", "Rocky", "Rishab", "Abhisek")

#set
student_set = set(students)
student_set.add("Robot")    
students1_set = set(students1)

print(f"Primary Student Set: {student_set}")
print(f"Secondary Student Set: {students1_set}")
print(f"Union (Total Unique): {student_set | students1_set}")
print(f"Intersection (Common Elements): {student_set & students1_set}")
print(f"Difference (Set 1 Exclusive): {student_set - students1_set}")
print(f"Symmetric Difference: {student_set ^ students1_set}")

print("\n Sorted\n")
for index, name in enumerate(sorted(student_set), 1):
    print(f"Record {index}: {name}")
print("\n--- Technical Verification: Mutability ---")
print(f"List (Mutable): Initial state maintained for {students[0]}")

try:
    fun_tuple[0] = "New Entry"
except TypeError:
    print("Tuple (Immutable): Modification rejected. Data integrity preserved.")

