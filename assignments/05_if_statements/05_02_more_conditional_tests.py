age = 20
has_license = True
temperature = 75
is_weekend = False

print("Is age > 18 and has_license? I predict True.")
print(age > 18 and has_license)

print("\nIs age > 30 and has_license? I predict False.")
print(age > 30 and has_license)

print("\nIs temperature > 70 or is_weekend? I predict True.")
print(temperature > 70 or is_weekend)

print("\nIs temperature < 60 or age < 18? I predict False.")
print(temperature < 60 or age < 18)

print("\nIs (age >= 21) and (has_license or is_weekend)? I predict False.")
print((age >= 21) and (has_license or is_weekend))