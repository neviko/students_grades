
from openpyxl import load_workbook
from students_grades.obj.student import Student
from students_grades.obj.course import Course

def get_students_grades(filename):
    student_obj_list = []
    wb = load_workbook(filename, read_only=True)
    ws = wb['FileFromYedion']

    for row in ws.rows:
        # Ignore the first two lines
        if row[0].row < 3:
            continue

        # Create list of student data [id, lastName, name, grade_1, grade_2]
        curr_student_list = []
        for cell in row:
            curr_student_list.append(cell.value)

        # The excel file is from right to left -> reverse
        reversed(curr_student_list)
        curr_student_obj = Student(curr_student_list)
        student_obj_list.append(curr_student_obj)

    return student_obj_list



if __name__ == '__main__':
    student_obj_list = get_students_grades('/Users/uria/Desktop/Semester b/מבוא לשפת פייתון/תרגילים להגשה/final project/YedionXlsFile_01271_03791.XLSX')

    for student in student_obj_list:
        student.print_student()