from datetime import datetime

# Get the current date and time
current_datetime = datetime.today()

# Format date and time as 'YYYY-MM-DD HH:MM:SS'
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

print(formatted_datetime)
