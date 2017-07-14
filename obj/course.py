class Course():
    def __init__(self, name, num_ex_required, weight_final_project, weight_exercises_dict=None):
        assert type(name) is str
        assert type(num_ex_required) is int
        assert type(weight_final_project) is float
        if weight_exercises_dict:
            assert all(type(weight) is float for weight in weight_exercises_dict.values())

        self.name = name
        self.num_ex_required = num_ex_required
        self.weight_final_project = weight_final_project
        self.weight_exercises_dict = weight_exercises_dict
        self.student_obj_list = []

    def add_student(self, student):
        self.student_obj_list.append(student)

    def set_exemptions(self, exemption_dict):
        for id, exemp in exemption_dict.items():
            for student in self.student_obj_list:
                if id == student.id:
                    student.set_exemption(exemp)

    def print_details(self):
        print('\nCourse:'
              '\n\tname: {}'
              '\n\tnumber exercises required: {}'
              '\n\tweight final project: : {}'
              '\n\tweight exercises dict: {}'
              '\n\n{}\n'
              .format(self.name, self.num_ex_required, self.weight_final_project,
                      self.weight_exercises_dict, '#' * 40))

        self.print_students()

    def print_students(self):
        print('\nStudents:\n')
        for student in self.student_obj_list:
            student.print_student()