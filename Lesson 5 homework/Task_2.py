import datetime


class PersonNew:
    def __init__(self, full_name="", yob=None):
        self.full_name = full_name
        self.yob = yob

        if len(self.full_name.split()) == 2:
            pass
        else:
            raise ValueError(
                "Incorrect 'full name' value. full name should content two worlds: 'NAME' + ' ' + 'SURNAME'")

        if 1900 <= self.yob <= datetime.datetime.now().year:
            pass
        else:
            raise ValueError("Incorrect 'yob' value. yob value should be <= current year and >= 1990")

    def getName(self):
        return f"Person's name: '{self.full_name.split()[0]}'"

    def getSurname(self):
        return f"Person's surname: '{self.full_name.split()[1]}'"

    def age_in(self, year=datetime.datetime.now().year):
        age_now = year - self.yob
        return f"Person's age is: {age_now}"


class EmployeeNew(PersonNew):
    def __init__(self, full_name="", yob=None, position="", w_exp=None, salary=None):
        PersonNew.__init__(self, full_name, yob)
        self.position = position
        self.w_exp = w_exp
        self.salary = salary

        if w_exp > 0:
            pass
        else:
            raise ValueError("'w_exp' value cannot not be negative")

        if salary > 0:
            pass
        else:
            raise ValueError("'salary' value cannot not be negative")

    def f_position(self):
        if self.w_exp > 6:
            return f"Position: Senior {self.position}"
        if 3 < self.w_exp <= 6:
            return f"Position: Middle {self.position}"
        if self.w_exp <= 3:
            return f"Position: Junior {self.position}"

    def raise_salary(self, income):
        return f"New salary: {self.salary + income}"


class ITEmployee(EmployeeNew):
    def __init__(self, *args, **kwargs):
        EmployeeNew.__init__(self, *args, **kwargs)
        self.skills = []

    def add_skill(self, new_skill):
        self.skills.append(new_skill)

    # def add_skills(self, new_skills):
    #     self.skills.append(new_skills)


if __name__ == "__main__":
    p = PersonNew("Roman Kniaziev", 1995)
    print(p.getName())
    print(p.getSurname())
    print(p.age_in())

    g = EmployeeNew("Roman Kniaziev", 1995, "QA", 100, 100)
    print(g.f_position())
    print(g.raise_salary(50))

    k = ITEmployee("Roman Kniaziev", 1995, "QA", 100, 100)
    k.add_skill("API")
    print(k.skills)
