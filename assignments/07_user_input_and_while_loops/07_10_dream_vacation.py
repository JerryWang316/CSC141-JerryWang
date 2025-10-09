# 7-10. Dream Vacation
print("DREAM VACATION POLL")
print("=" * 40)
print("Welcome to the Dream Vacation Poll!")
print("We're gathering data about people's ideal travel destinations.\n")

# Dictionary to store poll results
poll_results = {}
poll_active = True

while poll_active:
    # Get user's name
    name = input("What is your name? ").strip()
    
    # Get user's dream vacation destination
    dream_vacation = input("If you could visit one place in the world, where would you go? ").strip()
    
    # Store the response in the dictionary
    poll_results[name] = dream_vacation
    
    # Ask if another person wants to take the poll
    another = input("\nWould you like to let another person respond? (yes/no) ").strip().lower()
    if another != 'yes':
        poll_active = False
    
    print("-" * 40)

# Print the results of the poll
print("\n" + "=" * 50)
print("DREAM VACATION POLL RESULTS")
print("=" * 50)

if poll_results:
    print(f"Total respondents: {len(poll_results)}\n")
    
    print("Individual Responses:")
    print("-" * 30)
    for name, destination in poll_results.items():
        print(f"{name}: {destination.title()}")
    
    # Additional analysis
    print("\n" + "=" * 50)
    print("POPULAR DESTINATIONS ANALYSIS")
    print("-" * 35)
    
    # Count how many times each destination was mentioned
    from collections import Counter
    destination_counts = Counter(poll_results.values())
    
    # Find the most popular destination
    if destination_counts:
        most_common = destination_counts.most_common(1)[0]
        print(f"Most popular destination: {most_common[0].title()} (mentioned {most_common[1]} times)")
    
    print(f"Unique destinations mentioned: {len(destination_counts)}")
    
    # List all unique destinations
    print("\nAll dream destinations:")
    unique_destinations = sorted(list(set(poll_results.values())))
    for i, destination in enumerate(unique_destinations, 1):
        print(f"  {i}. {destination.title()}")
        
else:
    print("No responses were recorded.")

print("\nThank you for participating in our poll!")