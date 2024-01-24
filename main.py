# # For Loop
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)
#
# # List Comprehension
# new_list = [n + 1 for n in numbers]
# print(new_list)
#
# # String as List
# name = "Naseebullah Hoshmand"
# letters_list = [letter for letter in name]
# print(letters_list)
#
# # Range as List
# range_list = [n * 2 for n in range(1, 5)]
# print(range_list)
#
# # Conditional List Comprehension
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
#
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
#
# upper_case_names = [name.upper() for name in names if len(name) > 4]
# print(upper_case_names)

# # Dictionary Comprehension
# import random
# student_grades = {name: random.randint(1, 100) for name in names}
# print(student_grades)
#
# passed_students = {
#     student: grade
#     for (student, grade) in student_grades.items() if grade >= 60
# }
# print(passed_students)

# # Exercise
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day: (temp*9/5) + 32 for (day, temp) in weather_c.items()}
#
# print(weather_f)
#
from pandas import DataFrame
#
student_dict = {
    "Students": ["Jack", "John", "Peter"],
    "Scores": [32, 45, 65],
}
#
# for (key, value) in student_dict.items():
#     print(key, value)
#
df_student_dict = DataFrame(student_dict)
print(df_student_dict)
#
# # Loop through a data frame
# for (key, value) in df_student_dict.items():
#     print(key)
#     print(value)

# # Loop through rows of data frame
for (index, value) in df_student_dict.iterrows():
    print(index)
    print(value)
    print(value.Students)
    print(value.Scores)
    if value.Students == "John":
        print(value.Scores)