from datetime import datetime

# Normal working hours
start_hour = 9
end_hour = 17

# Get time from user
login_time_str = input("Type login time (HH:MM in 24hr format): ")

# Convert text to time
login_time = datetime.strptime(login_time_str, "%H:%M")

# Check if login is outside normal hours
if login_time.hour < start_hour or login_time.hour >= end_hour:
    print("Warning: Login is outside normal working hours!")
else:
    print("OK: Login is during normal working hours.")
