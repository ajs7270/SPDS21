class Schedule :
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    def __str__(self):
        return self.name + ", " + self.start + ", " + self.end

    def __lt__(self, other):
        if self.start < other.start:
            return True
        else :
            return False
     
class Calendar :
    def __init__(self):
        self.schedule_list = []

    def __str__(self):
        result =""

        self.schedule_list.sort()

        for idx, schedule in enumerate(self.schedule_list) :
            result += str(schedule) + '\n'
            if idx == 9:
                break
            

        return result 

    def _convert_time_to_int(self, time):
        day, hour = time.split()

        day = list(map(int,day.split('-')))
        hour = list(map(int, hour.split(':')))

        day = day[0]*10000 + day[1]*100 + day[2]
        hour = hour[0]*100 + hour[1]

        return day, hour
            
    def _check_time(self, time):
        # time type : "2021-04-05 09:35" , 
        target_day , target_time = self._convert_time_to_int(time)

        for schedule in self.schedule_list:
            start_day, start_time = self._convert_time_to_int(schedule.start)
            end_day, end_time = self._convert_time_to_int(schedule.end)
    
            if start_day <= target_day and target_day <= end_day:
                if start_time < target_time and target_time <= end_time:
                    
                    return schedule
        return None
        
    def add_schedule(self, name, start, end):
        if self._check_time(start) == None and self._check_time(end) == None:
            self.schedule_list.append(Schedule(name,start,end))
        else :
            raise ValueError

    def remove_schedule(self, time):
        schedule = self._check_time(time)

        if schedule is not None:
            self.schedule_list.remove(schedule)
        
    def check_schedule(self, time):
        schedule = self._check_time(time)

        if schedule is not None:
            return str(schedule)
        else:
            return ""

if __name__ == '__main__':
    calendar = Calendar()
    calendar.add_schedule('Lab meeting', '2021-04-05 13:00','2021-04-05 14:00')
    print(calendar)
    
    calendar.add_schedule('Lunch', '2021-04-05 12:00', '2021-04-05 13:00')
    calendar.add_schedule('Lunch', '2021-04-06 12:00', '2021-04-06 13:00')

    ret1 = calendar.check_schedule('2021-04-06 12:30')
    ret2 = calendar.check_schedule('2021-04-05 12:30')
    ret3 = calendar.check_schedule('2021-04-05 13:00')
    ret4 = calendar.check_schedule('2021-04-05 12:00')

    calendar.remove_schedule('2021-04-05 12:30')
    ret5 = calendar.check_schedule('2021-04-05 12:00')
    print(ret1)
    print(ret2)
    print(ret3)
    print(ret4)
    print(ret5)

    try:
        calendar.add_schedule('Homework', '2021-04-06 11:00', '2021-04-06 13:00')
    except ValueError:
        print("We have another schedule!")

    print(calendar)
