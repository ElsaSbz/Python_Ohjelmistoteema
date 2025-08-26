# Write a program that asks for the biological gender and hemoglobin value (g/l).
# The program the notifies the user if the hemoglobin value is low, normal or high.

# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.
Gender=input("What is your gender?")
Hemoglobin_value=float(input("What is your hemoglobin value?"))
if Gender == "male":
    if 134 <= Hemoglobin_value <= 167:
        print("the hemoglobin value is normal")
    elif Hemoglobin_value > 167:
        print("the hemoglobin value is high")
    else:
        print("the hemoglobin value is low")
elif Gender == "female":
    if 117 <= Hemoglobin_value <= 155:
        print("the hemoglobin value is normal")
    elif Hemoglobin_value > 155:
        print("the hemoglobin value is high")
    else:
        print("the hemoglobin value is low")
else:
    print("invalid input")
