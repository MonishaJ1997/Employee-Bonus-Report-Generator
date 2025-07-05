# Employee Bonus Report
employees = [("Asha", 95), ("Bala", 85), ("Charan", 70)]
for name, score in employees:
    if score >= 90:
        bonus = 10000
        status = "Excellent"
    elif score >= 75:
        bonus = 5000
        status = "Good"
    else:
        bonus = 2000
        status = "Needs Improvement"
    print(f"{name}: {status} → ₹{bonus}")

