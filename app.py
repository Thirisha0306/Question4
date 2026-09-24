
course_name = "Software Engineering"
student_count = 50
with open("build_report.txt", "w") as file:
file.write("Course Name: " + course_name + "\n")
file.write("Number of Students: " + str(student_count) + "\n")
print("Build report generated successfully.")