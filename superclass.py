from datetime import date, timedelta


class Employee:
    def __init__(self, name, surname, email, salary):
        self.name = name
        self.surname = surname
        self.email = email
        self.salary = salary

    def work(self):
        return '{} comes to the office!\n'.format(self.name)

    def check_salary(self, days):
        return '{} earns {} for {} days.\n'.format(self.name, self.salary*days, days)

    def month_salary(self):
        now = date.today()
        month_start = date(now.year, now.month, 1)
        weekend = [5, 6]
        diff = (now - month_start).days + 1
        day_count = 0

        for day in range(diff):
            # print((month_start + timedelta(day)).weekday())
            if (month_start + timedelta(day)).weekday() not in weekend:
                day_count += 1

        d = day_count
        return '{}`s month salary is {}.\n'.format(self.name, self.salary*d)

    def __str__(self):
        return '{}: {} {}\n'.format(self.__class__.__name__, self.name, self.surname)

    def comparison(self, other):
        if self.salary > other.salary:
            return '{} > {}'.format(self.name, other.name)
        elif self.salary < other.salary:
            return '{} < {}'.format(self.name, other.name)
        elif self.salary == other.salary:
            return '{} = {}'.format(self.name, other.name)
