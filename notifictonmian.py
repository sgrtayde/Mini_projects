import time
from plyer import notification

def water_reminder():
    while True:
        notification.notify(
            title="Water Reminder for Sagar",
            message="Time to sip some water!",
            timeout=10
        )
        # time.sleep(3600)  # 1 hour
        time.sleep(3)  # 3 seconds for testing purposes

if __name__ == "__main__":
    water_reminder()
