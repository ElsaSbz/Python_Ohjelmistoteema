#This exercise continues the previous car race exercise from the last exercise set.
# Write a Race class that has the following properties: name, distance in kilometers and a list of cars participating in the race.
# The class has an initializer that receives the name, kilometers, and car list as parameters and sets their values to the corresponding properties in the class.
# The class has the following methods:
#hour_passes, which performs the operations done once per hour in the original exercise: generates a random change of speed for each car and calls their drive method.
#print_status, which prints out the current information of each car as a clear, formatted table.
#race_finished, which returns True if any of the cars has reached the finish line, meaning that they have driven the entire distance of the race.
#Write a main program that creates an 8000-kilometer race called Grand Demolition Derby. The new race is given a list of ten cars similarly to the earlier exercise. The main program simulates the progressing of the race by calling the hour_passes in a loop, after which it uses the race_finished method to check if the race has finished. The current status is printed out using the print_status method every ten hours and then once more at the end of the race.



import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0  # Automatically set to zero
        self.travelled_distance = 0  # Automatically set to zero

    def accelerate(self, change):
        new_speed = self.current_speed + change
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self):
        # Update travelled distance based on current speed (assume 1 hour of driving)
        self.travelled_distance += self.current_speed


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            # Generate a random change in speed between -10 km/h and +15 km/h
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive()  # Move the car for one hour

    def print_status(self):
        print(f"\nRace: {self.name}")
        print(
            f"{'Registration Number':<20}{'Max Speed (km/h)':<20}{'Current Speed (km/h)':<20}{'Travelled Distance (km)':<25}")
        print("=" * 85)
        for car in self.cars:
            print(
                f"{car.registration_number:<20}{car.max_speed:<20}{car.current_speed:<20}{car.travelled_distance:<25}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)


# Main program to simulate the race
if __name__ == "__main__":
    # Create a list of 10 cars for the race
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)  # Random max speed between 100 and 200 km/h
        registration_number = f"ABC-{i}"
        cars.append(Car(registration_number, max_speed))

    # Create an 8000-kilometer race called Grand Demolition Derby
    race = Race("Grand Demolition Derby", 8000, cars)

    hours_passed = 0
    while not race.race_finished():
        race.hour_passes()
        hours_passed += 1

        # Print status every 10 hours
        if hours_passed % 10 == 0:
            race.print_status()

    # Final status at the end of the race
    race.print_status()
    print("\nThe race is finished!")