import json
import os
import threading
import time

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from plyer import notification
from kivy.core.audio import SoundLoader

from scheduler import schedule_daily_reminder

SETTINGS_FILE = 'settings.json'

DEFAULT_TASKS = [
    "Schedule meetings",
    "Book reservations",
    "Summarize reports",
    "Order groceries",
    "Review emails"
]

DEFAULT_TIME = "07:00"


def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as f:
            return json.load(f)
    else:
        return {"tasks": DEFAULT_TASKS, "time": DEFAULT_TIME}


def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=4)


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.settings = load_settings()

        self.task_inputs = []

        self.add_widget(Label(text="📝 Edit Your Daily Tasks:", size_hint_y=None, height=40))

        scroll = ScrollView(size_hint=(1, 0.6))
        task_container = BoxLayout(orientation='vertical', size_hint_y=None)
        task_container.bind(minimum_height=task_container.setter('height'))

        for task in self.settings['tasks']:
            input_field = TextInput(text=task, multiline=False, size_hint_y=None, height=40)
            self.task_inputs.append(input_field)
            task_container.add_widget(input_field)

        scroll.add_widget(task_container)
        self.add_widget(scroll)

        self.add_widget(Label(text="⏰ Set Reminder Time (24h format HH:MM):", size_hint_y=None, height=40))
        self.time_input = TextInput(text=self.settings['time'], multiline=False, size_hint_y=None, height=40)
        self.add_widget(self.time_input)

        save_button = Button(text="💾 Save Settings", size_hint_y=None, height=50)
        save_button.bind(on_press=self.save_settings)
        self.add_widget(save_button)

        self.status_label = Label(text="", size_hint_y=None, height=30)
        self.add_widget(self.status_label)

    def save_settings(self, instance):
        updated_tasks = [inp.text.strip() for inp in self.task_inputs if inp.text.strip()]
        updated_time = self.time_input.text.strip()

        if not updated_time or len(updated_time) != 5 or updated_time[2] != ":":
            self.status_label.text = "[color=ff0000]Invalid time format. Use HH:MM[/color]"
            return

        self.settings['tasks'] = updated_tasks
        self.settings['time'] = updated_time
        save_settings(self.settings)

        self.status_label.text = "[color=00ff00]Settings saved successfully![/color]"

        # Restart scheduler with new settings
        App.get_running_app().reset_reminder()


class MDApp(App):
    def build(self):
        self.settings = load_settings()
        schedule_daily_reminder(self.settings)
        return MainScreen()

    def reset_reminder(self):
        self.settings = load_settings()
        schedule_daily_reminder(self.settings)


if __name__ == "__main__":
    MDApp().run()
