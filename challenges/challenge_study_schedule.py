def study_schedule(permanence_period, target_time):
    # deacordo com course usando linear search
    if type(target_time) != int:
        return None

    students_at_same_time = 0

    n = len(permanence_period)
    for index in range(0, n):
        if (
            type(permanence_period[index][0]) != int
            or type(permanence_period[index][1]) != int
        ):
            return None

        if (
            permanence_period[index][0]
            <= target_time
            <= permanence_period[index][1]
        ):
            students_at_same_time += 1
    return students_at_same_time
