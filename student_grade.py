
from openpyxl import load_workbook
from students_grades.obj.student import Student
from students_grades.obj.course import Course

def generate_students_obj(grades_filename):
    student_obj_list = []
    wb = load_workbook(grades_filename, read_only=True)
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


def generate_exemption_dict(exemp_filename):
    exemption_dict = {}
    wb = load_workbook(exemp_filename, read_only=True)
    ws = wb['Sheet1']

    for row in ws.rows:
        # Ignore the first line
        if row[0].row == 1:
            continue

        id = row[0].value
        assert type(id) is int

        exemp = row[2].value
        exemption_dict[id] = exemp

    return exemption_dict


if __name__ == '__main__':
    course_name = 'עקרונות התכנות בפייתון'
    course = Course(course_name, 5, 0.4)

    course.student_obj_list = generate_students_obj('/Users/uria/Desktop/Semester b/מבוא לשפת פייתון/תרגילים להגשה/final project/YedionXlsFile_01271_03791.XLSX')

    course.set_exemptions(generate_exemption_dict('/Users/uria/Desktop/Semester b/מבוא לשפת פייתון/תרגילים להגשה/final project/מחר פטורים.xlsx'))

    course.print_details()