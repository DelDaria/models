from superclass import Employee


class Recruiter(Employee):
    def __init__(self, name, surname, email, salary, hired_this_month):
        super().__init__(name, surname, email, salary)
        self.hired = hired_this_month

    def work(self):
        emp_work = super().work()[:-2]
        return emp_work + ' for hiring!'


class Programmer(Employee):
    def __init__(self, name, surname, email, salary, closed_this_month):
        super().__init__(name, surname, email, salary)
        self.closed = closed_this_month
        self.tech = []

    def work(self):
        emp_work = super().work()[:-1]
        return emp_work + ' for coding!'

    def add_tech(self, skill):
        self.tech.append(skill)

    def tech_stack(self):
        return '{}: {}'.format(self.name, self.tech)

    def comparison_tech(self, other):
        if len(self.tech) > len(other.tech):
            return '{} > {}'.format(self.name, other.name)
        elif len(self.tech) < len(other.tech):
            return '{} < {}'.format(self.name, other.name)
        elif len(self.tech) == len(other.tech):
            return '{} = {}'.format(self.name, other.name)

    def alpha_programmer(self, other):
        for i in self.tech:
            if i not in other.tech:
                other.tech.append(i)
        return 'Alpha-programmer`s tech stack: {}.'.format(other.tech)


class Candidate(Employee):
    def __init__(self, name, surname, email, salary, technologies, main_skill, main_skill_grade):
        super().__init__(name, surname, email, salary)
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade


class Vacancy:
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level
