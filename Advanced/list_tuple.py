# List vs Tuple : List can be resized but not tuple

# s1 = "Shreyas"
# s2 = "Devrikh"
# s3 = "Inarat"
# s4 = "Sumedha"
#
# print(s1)
# print(s2)
# print(s3)
# print(s4)


student_names1 = ["Shreyas", "Devrikh", "Inarat", "Sumedha"]

print(type(student_names1))  # list

student_names2 = ("Shreyas", "Devrikh", "Inarat", "Sumedha")

print(type(student_names2))  # tuple

student_names1.append("Vibhansh")
student_names1.append("Sanika")

print(student_names1[2])
print(len(student_names1))

student_names1.append("Chirag")
print(student_names1)
print(len(student_names1))

student_names1.remove("Vibhansh")
student_names1.remove("Sanika")

print(student_names1)
print(len(student_names1))
new_students = (student_names1[0:3])
print(new_students)

nums = [1, 5, 9, 2, 4, 15, 12, 16, 14, 7]
nums.sort()
print(nums)

print(student_names1[0] + " " + student_names1[3])

alphanums = ["a", 2, "d", 3]
print(alphanums)
print(alphanums[1])
