class Student():
    def __init__(self, student_data_list):
        self.id = student_data_list[0]
        assert type(self.id) is int

        self.name = student_data_list[1]
        self.last_name = student_data_list[2]

        self.ex_grade_list = student_data_list[3:]
        self.ex_grade_list = [grade if grade else 0 for grade in self.ex_grade_list]
        assert all(type(ex) is int for ex in self.ex_grade_list)

        self.exemption_list = []
        self.final_project_grade = None
        self.final_grade = None

    def set_exemption(self, exemp):
        # Range
        if '-' in exemp:
            exemp = exemp.split('-')
            assert len(exemp) == 2

            num_1 = int(exemp[0])
            num_2 = int(exemp[1])

            self.exemption_list = list(range(num_1, num_2 + 1))

        # Type list
        elif type(exemp) == list:
            assert all(type(ex) is int for ex in exemp)
            self.exemption_list = exemp

        # One number
        else:
            assert type(exemp) is int
            self.exemption_list.append(exemp)

    def print_student(self):
        print('{}, {}, {}\n{}\nExemptions: {}\n'
              .format(self.id, self.name, self.last_name, self.ex_grade_list, self.exemption_list))