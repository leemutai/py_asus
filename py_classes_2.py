from datetime import datetime, date


class Person:
    def __init__(self, name, email, dob, gender, favorite_teams):
        self.name = name
        self.email = email
        self.dob = dob
        self.gender = gender
        self.teams = favorite_teams

    def print_details(self):
        print(self.name)
        print(self.gender)
        print(self.email)
        print("-----Teams-----")
        for team in self.teams:
            print(team)
        print("----------")
        # "10-09-2001"

    def calc_age(self):
        today = datetime.now()
        dob = datetime.strptime(self.dob, "%d-%m-%Y")
        delta = today - dob
        print(delta.days // 365) , "Years Old" # calculate the age in years


p1 = Person("June", "june@test.com", "13-09-1999", "Female", ["Newcastle", "Girong"])
p1.print_details()
p1.calc_age()
