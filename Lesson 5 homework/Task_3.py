import datetime


class RecParam:
    def __init__(self, side_a=None, side_b=None):

        """
        Counts the parameters of the rectangle
                Parameters:
                    side_a (int): first side
                    side_b (int): second side
        """
        self.side_a = side_a
        self.side_b = side_b

    def rec_perimeter(self):
        """Calculate rectangle's perimeter"""
        return 2 * (self.side_a + self.side_b)

    def rec_area(self):
        """Calculate rectangle's area"""
        return self.side_a * self.side_b


class Student:
    def __init__(self, full_name, speciality, yos, grades=[]):
        """Some operation with students info
            Parameters:
                full_name (str): first name and surname
                speciality (str): students speciality
                yos (int): year of study starting
                grades (list): list of grades
        """
        self.full_name = full_name
        self.speciality = speciality
        self.yos = yos
        self.grades = grades

    def __str__(self):
        return f"Grades: {self.grades}"

    def add_grade(self, new_grade):
        """Add grade to grades list"""
        self.grades.append(new_grade)

    def a_score(self):
        """
        Displays the average grade for the grades
        """
        sum1 = 0
        for i in self.grades:
            sum1 = sum1 + i
        return sum1 // len(self.grades)

    def how_m_years(self):
        """
        Counts how many years a student has studied from the year of the beginning of his studies
        """
        return datetime.datetime.now().year - self.yos


class MapPoint:
    def __init__(self, px, py):
        """Calculations with coordinate points
                Parameters:
                    px (int): x point
                    py (int): y point
        """
        self.px = px
        self.py = py

    def null_distance(self):
        (self.px ** 2 + self.py ** 2) // 0.5

    def __str__(self):
        return f"Distance: {((self.px ** 2) + (self.py ** 2)) ** 0.5}"


if __name__ == "__main__":
    a = RecParam(25, 32)
    print(a.rec_area())
    print(a.rec_perimeter())

    b = Student("Roman Kniaziev", "math", 2005, [2, 4, 5, 3, 2])
    b.add_grade(5)
    print(b)
    print(b.a_score())
    print(b.how_m_years())

    c = MapPoint(-5, 12)
    print(c)
