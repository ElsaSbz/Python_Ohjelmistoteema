import Elevator
import Building
#exercise 1
# Test the class by creating an elevator in the main program, tell it to move to a floor of your choice and then back to the bottom floor.

elevator = Elevator.Elevator(1, 10)
print("Moving to floor 5:")
elevator.go_to_floor(5)
print("\nReturning to the bottom floor:")
elevator.go_to_floor(1)

#exercise 2
#In the main program, write the statements for creating a new building and running the elevators of the building.
building = Building.Building(1, 10, 3)
building.run_elevator(1, 5)
building.run_elevator(2, 10)
building.run_elevator(3, 3)
building.run_elevator(1, 1)

#exercise 3
#Continue the main program by causing a fire alarm in your building.
building.fire_alarm()
