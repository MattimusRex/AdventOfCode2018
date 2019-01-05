import datetime

class TimeStampedAction:  
    def __init__(self, string):
        parts = string.split(']')
        parts = [part.strip('[').strip() for part in parts]
        timestamp = parts[0].split()
        date = [int(part) for part in timestamp[0].split('-')]
        time = [int(part) for part in timestamp[1].split(':')]
        self.timestamp = datetime.datetime(date[0], date[1], date[2], time[0], time[1])
        self.action = parts[1]

# process input into objects to sort in chronological order
actions = []
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        actions.append(TimeStampedAction(line))
actions.sort(key=lambda x: x.timestamp)

# find guard that sleeps the most
sleep_time = {}
minutes_count = {}
for action in actions:
    action_parts = action.action.split()
    if action_parts[0] == 'Guard':
        current_guard = int(action_parts[1].strip('#'))
    elif action_parts[0] == 'falls':
        sleep_start = action.timestamp
    elif action_parts[0] == 'wakes':
        minutes = (action.timestamp - sleep_start).seconds / 60
        sleep_time[current_guard] = sleep_time.get(current_guard, 0) + minutes
        if current_guard not in minutes_count:
            minutes_count[current_guard] = [0] * 60
        start_minute = sleep_start.minute
        end_minute = action.timestamp.minute
        for minute in range(start_minute, end_minute):
            minutes_count[current_guard][minute] += 1

max_sleep_time = 0
for entry in sleep_time:
    minutes = sleep_time[entry]
    if minutes > max_sleep_time:
        max_sleep_time = minutes
        max_guard = entry

sleepiest_minute = max(minutes_count[max_guard])
sleepiest_minute = minutes_count[max_guard].index(sleepiest_minute)
print(sleepiest_minute * max_guard)
        