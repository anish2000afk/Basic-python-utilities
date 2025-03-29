import schedule  # Import the schedimport schedule  # Import the schedule library for task scheduling
import time
from plyer import notification
from datetime import datetime, timedelta


def send_notification(amount, time_slot):
    """Sends a desktop notification with the water reminder."""
    notification.notify(
        title="Water Reminder",
        message=f"Time to drink {amount} ml of water ({time_slot})",
        app_name="Water Tracker",
    )


# Schedule water intake notifications covering the entire day (converted to 24-hour format)
time_slots = {
    "04:00": 200,
    "05:00": 200,
    "06:00": 250,
    "07:00": 250,
    "08:00": 250,
    "09:00": 250,
    "10:00": 250,
    "11:00": 250,
    "12:00": 200,
    "13:00": 200,
    "14:00": 200,
    "15:00": 200,
    "16:00": 200,
    "17:00": 200,
    "18:00": 200,
    "19:00": 200,
    "20:00": 150,
    "21:00": 150,
    "22:00": 100,  # Less water intake at night
}

# Schedule the notifications for each time slot
for time_slot, amount in time_slots.items():
    schedule.every().day.at(time_slot).do(send_notification, amount, time_slot)

# Run the scheduler in a loop
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minutenute
