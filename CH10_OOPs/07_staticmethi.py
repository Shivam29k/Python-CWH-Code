class Employee:
    company = 'Google'

    # by using static method u stop the code to create an argument, so essliye self likn ki jarurat nai hoti
    @staticmethod
    def greet():
        print("good morning, Sir")


harry = Employee()

harry.greet()
