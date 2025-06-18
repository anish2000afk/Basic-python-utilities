import datetime
import time
import os


def generate_schedule(start_hour=6, start_minute=30, blocks=16):
    schedule = {}
    current = datetime.datetime.combine(
        datetime.date.today(), datetime.time(start_hour, start_minute)
    )

    # Original 16 blocks (40-min lecture + 20-min test)
    for i in range(1, blocks + 1):
        lecture_time = (current.hour, current.minute)
        schedule[lecture_time] = f"Block {i} - 40 min Lecture"
        current += datetime.timedelta(minutes=40)

        test_time = (current.hour, current.minute)
        schedule[test_time] = f"Block {i} - 20 min Test"
        current += datetime.timedelta(minutes=20)

    # Extra 30-min lecture at 10:30 PM
    extra_lecture_time = (current.hour, current.minute)
    schedule[extra_lecture_time] = "Extra Block - 30 min Lecture"
    current += datetime.timedelta(minutes=30)

    # Workout reminder at 11:00 PM
    workout_time = (current.hour, current.minute)
    schedule[workout_time] = "Get ready to workout!"

    return schedule


schedule_map = generate_schedule()
executed_today = set()


def notify(task):
    now_str = datetime.datetime.now().strftime("%H:%M")
    print(f"[{now_str}] ⏰ {task}")
    os.system(f'notify-send -u critical -t 0 "Task Reminder" "{task}"')


def check_and_run():
    now = datetime.datetime.now()
    current_time = (now.hour, now.minute)
    if current_time in schedule_map and current_time not in executed_today:
        notify(schedule_map[current_time])
        executed_today.add(current_time)


def reset_executed():
    now = datetime.datetime.now()
    if now.hour == 0 and now.minute == 0:
        executed_today.clear()


while True:
    check_and_run()
    reset_executed()
    time.sleep(60)
