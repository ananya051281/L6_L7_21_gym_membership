
import math


def parse_plan(code):
    if not isinstance(code, str):
        return None

    parts = code.strip().split('-')

    if len(parts) != 2:
        return None

    plan, months = parts

    if not plan.strip() or not months.strip():
        return None

    try:
        months = int(months)
        if months <= 0:
            return None
    except ValueError:
        return None

    return plan.strip().upper(), months


def calculate_bmi(data):
    if not isinstance(data, str):
        return None

    parts = data.split(',')

    if len(parts) != 2:
        return None

    try:
        weight = float(parts[0].strip())
        height = float(parts[1].strip())

        if not math.isfinite(weight) or not math.isfinite(height):
            return None

        if weight <= 0 or height <= 0:
            return None

        return round(weight / (height ** 2), 1)

    except (ValueError, OverflowError):
        return None


def average_workout(minutes):
    if not isinstance(minutes, str):
        return None

    values = minutes.split()

    if not values:
        return None

    try:
        values = [int(m) for m in values]

        if any(m < 0 for m in values):
            return None

        return sum(values) // len(values)

    except ValueError:
        return None


def main():
    print("==== Running parse_plan ====")
    user_input = input("Enter a plan code (e.g. GOLD-12): ")
    result = parse_plan(user_input)
    print("Plan and Months:", result if result is not None else "Invalid input")

    print("\n==== Running calculate_bmi ====")
    user_input = input("Enter weight and height (e.g. 70,1.75): ")
    result = calculate_bmi(user_input)
    print("BMI:", result if result is not None else "Invalid input")

    print("\n==== Running average_workout ====")
    user_input = input("Enter workout minutes separated by spaces (e.g. 45 60 30): ")
    result = average_workout(user_input)
    print("Average Minutes:", result if result is not None else "Invalid input")


if __name__ == "__main__":
    main()
