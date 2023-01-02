# Write a class Train which has methods to book a ticket, get status(no of seats), and get fare information of trains running under Indian Railways.

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def ticketBooking(self):
        if self.seats > 0:
            print(
                f'Your ticket has been booked and your seat number is {self.seats}')
            self.seats -= 1
        else:
            print('Sorry but train is full pehale book karnae ka.')

    def getStatus(self):
        print(f'The name of the train is {self.name}')
        print(f'Seats available in the train are {self.seats}')

    def fareInfo(self):
        print(f'Prize of the the ticket is: Rs {self.fare}')


intercity = Train('Intercity Express', 400, 1)

intercity.fareInfo()
intercity.getStatus()
intercity.ticketBooking()
intercity.getStatus()
intercity.ticketBooking()

