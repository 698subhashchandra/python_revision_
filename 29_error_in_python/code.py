def divide(dividend, divisor):
    if divisor ==  0:
        print("Divisor cannot be 0.")
        return

    return dividend / divisor






students = [
    {"name": "Bob", "grades": [75, 85]},
    {"name": "Rolf", "grades": [100, 45]},
    {"name": "Anne", "grades": [65, 85]},
    {"name": "Jen", "grades": [95, 75]},
    {"name": "Denial", "grades": [85, 25]},
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError:
    print(f'ERROR: {name} has no grades!')
else:
    print("-- ALL STUDENT AVERAGES CALCULATED ---")
finally:
    print("--- END OF STUDENT AVERAGE CALCULATION ---")
