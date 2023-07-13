def study_schedule(permanence_period, target_time):
    count = 0
    if target_time is None or target_time == 0:
        return None
    for hour in permanence_period:
        if not isinstance(hour[0], int) or not isinstance(hour[1], int):
            count = None
            break
        else:
            if hour[0] <= target_time <= hour[1]:
                count += 1
    return count
