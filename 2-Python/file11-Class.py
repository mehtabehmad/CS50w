class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(2, 8)
print(p.x)
print(p.y)

print("----------------------------------\n")


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight1 = Flight(3)
passengers = ["harry", "ron", "draco", "ginny"]
for passenger in passengers:
    success = flight1.add_passenger(passenger)

    # you can directly add flight1.add_passenger(passenger) to the if line instead of success variable
    if success:
        print(f'Added {passenger.capitalize()} to flight successfully.')
    else:
        print(f'No available seats for {passenger.capitalize()}.')

print("\n----------------------------------")
    