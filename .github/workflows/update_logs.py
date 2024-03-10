from datetime import datetime

# Define the path to the logs file
log_file_path = "logs.txt"

# Get the current time
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Write the current time to the logs file
with open(log_file_path, "a") as file:
    file.write(current_time + "\n")
