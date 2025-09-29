def determine_life_stage(age):
    """Determine and return the life stage based on age"""
    if age < 2:
        return "baby", "less than 2 years old"
    elif age < 4:
        return "toddler", "at least 2 but less than 4 years old"
    elif age < 13:
        return "kid", "at least 4 but less than 13 years old"
    elif age < 20:
        return "teenager", "at least 13 but less than 20 years old"
    elif age < 65:
        return "adult", "at least 20 but less than 65 years old"
    else:
        return "elder", "65 years or older"

# Test a range of ages
print("=== DETAILED LIFE STAGES ===")
test_ages = [1, 2, 3, 8, 14, 19, 25, 64, 65, 80]

for age in test_ages:
    stage, description = determine_life_stage(age)
    print(f"Age {age}: {stage.title()} ({description})")