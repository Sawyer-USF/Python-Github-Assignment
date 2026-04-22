# Display a welcome message so the user knows the program has started.
print("Welcome to my Python program!")

# Ask the user how many hours they studied today.
hours = input("How many hours did you study today? ")

# Convert the input to a number and handle invalid entries safely.
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    raise SystemExit(1)

# Estimate the total number of study hours for one week.
weekly_hours = hours * 7

# Show the result in clear language.
print(f"You are on track to study {weekly_hours:.1f} hours this week.")
