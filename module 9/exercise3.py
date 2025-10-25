#Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
# The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
# Example: The travelled distance of car object is 2000 km.
# The current speed is 60 km/h. Method call car.drive(1.5) increases the travelled distance to 2090 km.

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, new_speed):
            if new_speed <= 0 and new_speed + self.current_speed >= 0:
                self.current_speed += new_speed
            elif new_speed > 0 and new_speed + self.current_speed <= self.maximum_speed:
                self.current_speed += new_speed
            else :
                print("Warning! Speed could not be changed!")
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

new_car = Car ("ABC-123",142)
new_car.accelerate(60)
new_car.travelled_distance = 2000
new_car.drive(1.5)
print(new_car.travelled_distance)