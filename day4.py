from pathlib import Path


def bubble_sort(l, type):
    test = set()
    if type == 'mon':
        for iter_num in range(len(l) - 1, 0, -1):
            for i in range(iter_num):
                set.add(l[i][6:8])
                if int(l[i][6:8]) > int(l[i + 1][6:8]):
                    temp = l[i]
                    l[i] = l[i + 1]
                    l[i + 1] = temp
    print('set length = ', len(test))

    if type == 'day':
        for iter_num in range(len(l) - 1, 0, -1):
            for i in range(iter_num):
                if int(l[i][9:11]) > int(l[i + 1][9:11]):
                    temp = l[i]
                    l[i] = l[i + 1]
                    l[i + 1] = temp


sleep_schedule = Path('day4.in.txt').read_text().split('\n')
bubble_sort(sleep_schedule, 'mon')
bubble_sort(sleep_schedule, 'day')
bubble_sort(sleep_schedule, 'time')

guards = {}
# date = date "yyyy-mm-dd"
# time = time "hh:mm"
# info = information about what is the current action taking place
# ie. Who has the shift, if the guard is falling asleep or wakes up.

q = []
time_asleep = 0
previous_guard = -1

for guard_info in sleep_schedule:

    date_and_time, info = guard_info.rsplit(']', 1)
    date_and_time = date_and_time[1:]
    date, time = date_and_time.rsplit(' ', 1)
    info = info.lstrip().split(' ')
    info = [x.lower() for x in info]
    guard = int

    if info[0] == 'guard':
        guard = int(info[1][1:])
        q.append(guard)
        previous_guard = guard

    elif info[0] == 'wakes':
        if len(q) == 1:
            time_asleep = int(time.split(':')[1]) - (q.pop(0))
        else:
            guard = q.pop(0)
            time_asleep = int(time.split(':')[1]) - (q.pop(0))

        if previous_guard not in guards.keys():
            guards[previous_guard] = time_asleep
        else:
            time_asleep += guards[previous_guard]
            guards[previous_guard] = time_asleep

    elif info[0] == 'falls':
        q.append(int(time.split(':')[1]))

for key in guards.keys():
    print('guard # ', key, ' has been asleep for : ', guards[key], 'minutes')
