#Extend the program by adding an accelerate method into the new class.
# The method should receive the change of speed (km/h) as a parameter.
# If the change is negative, the car reduces speed.
# The method must change the value of the speed property of the object.
# The speed of the car must stay below the set maximum and cannot be less than zero.
# Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h.
# Then print out the current speed of the car.
# Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed.
# The travelled distance does not have to be updated yet.

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

new_car = Car ("ABC-123",142)
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
print(f".Current speed of the new car is: {new_car.current_speed}")
new_car.accelerate(-200)
print(f".Current speed after emergency brake is: {new_car.current_speed}")