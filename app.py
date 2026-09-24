
import os

def create_report():
    course_name = "Cloud Architecture 101"
    
    student_count = os.getenv('STUDENT_COUNT', '25') 
    
    with open("build_report.txt", "w") as f:
        f.write(f"Course Name: {course_name}\n")
        f.write(f"Students Enrolled: {student_count}\n")
    
    print("build_report.txt generated successfully.")

if __name__ == "__main__":
    create_report()
