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

# track minutes guards are asleep
minutes_count = {}
for action in actions:
    action_parts = action.action.split()
    if action_parts[0] == 'Guard':
        current_guard = int(action_parts[1].strip('#'))
    elif action_parts[0] == 'falls':
        sleep_start = action.timestamp
    elif action_parts[0] == 'wakes':
        if current_guard not in minutes_count:
            minutes_count[current_guard] = [0] * 60
        start_minute = sleep_start.minute
        end_minute = action.timestamp.minute
        for minute in range(start_minute, end_minute):
            minutes_count[current_guard][minute] += 1

max_minute = 0
for guard in minutes_count:
    guards_max_minute = max(minutes_count[guard])
    if guards_max_minute > max_minute:
        max_index = minutes_count[guard].index(guards_max_minute)
        max_minute = guards_max_minute
        max_guard = guard

print(max_guard)
print(max_index)
print(max_guard * max_index)

        