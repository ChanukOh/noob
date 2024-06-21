import datetime

def solution(a, b):
    date_2016 = datetime.date(2016, 1, 1)
    target_date = datetime.date(2016, a, b)
    day_of_week = target_date.weekday()
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    answer = days[day_of_week]
    return answer