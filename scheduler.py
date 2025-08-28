import threading
import time
from plyer import notification
from kivy.core.audio import SoundLoader


def show_notification(tasks):
    notification.notify(
        title="🛎️ MD Daily Reminder",
        message="\n".join(tasks),
        timeout=10
    )
    sound = SoundLoader.load('assets/alert.wav')
    if sound:
        sound.play()


def schedule_daily_reminder(settings):
    def alarm_loop():
        while True:
            current_time = time.strftime("%H:%M")
            if current_time == settings["time"]:
                show_notification(settings["tasks"])
                time.sleep(60)  # Avoid multiple triggers in the same minute
            time.sleep(20)

    # Run in background daemon thread
    thread = threading.Thread(target=alarm_loop, daemon=True)
    thread.start()
