from datetime import datetime
def solution(a, b):
    
    target = datetime(2016, int(a), int(b))
    
    day = target.weekday()
    day_dict = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    
    return day_dict[day]