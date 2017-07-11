class Student():
    def __init__(self, student_data_list):
        self.id = student_data_list[0]
        self.name = student_data_list[1]
        self.last_name = student_data_list[2]

        self.ex_grade_list = student_data_list[3:]
        self.exemption_list = []
        self.final_project_grade = None
        self.final_grade = None


    def print_student(self):
        print('{}, {}, {}\n{}\n' .format(self.id, self.name, self.last_name, self.ex_grade_list))