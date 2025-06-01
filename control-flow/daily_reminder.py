# daily_reminder.py

# Prompt the user for the task details
task = input("Enter your task for today: ")
priority = input("What is the priority of this task? (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Simple loop to simulate a checking/loading reminder
print("\nProcessing your task", end="")
for i in range(3):
    print(".", end="")
print("\n")

# Match case for priority level
match priority:
    case "high":
        message = f"⚠️ High-priority task: '{task}'"
    case "medium":
        message = f"🔔 Medium-priority task: '{task}'"
    case "low":
        message = f"📝 Low-priority task: '{task}'"
    case _:
        message = f"❓ Unknown-priority task: '{task}'"

# Add urgency if the task is time-bound
if time_bound == "yes":
    message += " — that requires immediate attention today!"

# Display the customized reminder
print(message)
