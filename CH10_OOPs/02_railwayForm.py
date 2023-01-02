class RailwayForm:
    formType = "RailwayForm"

    def printData(self):
        print(f'Name is {self.name}')
        print(f'Train name is {self.train}')


shivamApplicationForm = RailwayForm()
shivamApplicationForm.name = 'Shivam Kumar'
shivamApplicationForm.train = 'Amritsar Express'
shivamApplicationForm.printData()
