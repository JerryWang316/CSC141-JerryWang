# Extended person dictionary with additional information
person = {
    'first_name': 'Tianrui',
    'last_name': 'Wang',
    'age': 20,
    'city': 'Hong Kong',
    'occupation': 'Business Student',
    'university': 'University of Hong Kong',
    'hobbies': ['basketball', 'travelling', 'photography', 'singing'],
    'languages': ['Python', 'Mandarin', 'English', 'Cantonese'],
    'email': 'tianrui.wang@example.com',
    'website': 'portfolio.tianrui.dev'
}

print("=" * 50)
print("PERSONAL PROFILE")
print("=" * 50)

# Basic Information Section
print("\n📋 BASIC INFORMATION")
print("-" * 30)
print(f"👤 Name: {person['first_name']} {person['last_name']}")
print(f"🎂 Age: {person['age']}")
print(f"📍 Location: {person['city']}")

# Professional Information Section
print("\n💼 PROFESSIONAL INFORMATION")
print("-" * 35)
print(f"💼 Occupation: {person['occupation']}")
print(f"🎓 University: {person['university']}")

# Skills and Languages Section
print("\n🔧 SKILLS & LANGUAGES")
print("-" * 25)
print("💻 Programming Languages:")
for lang in person['languages'][:3]:  # First 3 are programming languages
    print(f"   • {lang}")

print("🗣️ Spoken Languages:")
for lang in person['languages'][3:]:  # Last 3 are spoken languages
    print(f"   • {lang}")

# Hobbies Section
print("\n🎯 HOBBIES & INTERESTS")
print("-" * 25)
for hobby in person['hobbies']:
    print(f"   • {hobby.title()}")

# Contact Information Section
print("\n📞 CONTACT INFORMATION")
print("-" * 25)
print(f"📧 Email: {person['email']}")
print(f"🌐 Website: {person['website']}")

# Additional calculated information
print("\n📊 ADDITIONAL INFORMATION")
print("-" * 25)
print(f"🎨 Number of hobbies: {len(person['hobbies'])}")
print(f"🗣️ Languages spoken: {len(person['languages'][3:])}")
print(f"💻 Programming languages known: {len(person['languages'][:3])}")

print("\n" + "=" * 50)
print("PROFILE COMPLETE")
print("=" * 50)