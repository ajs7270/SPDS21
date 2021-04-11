from prob1 import Calendar, Schedule

class SmartCalendar(Calendar):
    def __init__(self):
        super().__init__()
        self.daily_schedule = []

    def __str__(self):
        result = ""

        printing_schedule_list = []

        day_list = ['2021-04-05','2021-04-06','2021-04-07','2021-04-08',
                '2021-04-09', '2021-04-10', '2021-04-11',
                '2021-04-12', '2021-04-13', '2021-04-14']

        for day in day_list:
            for schedule in self.daily_schedule :
                printing_schedule_list.append(
                    Schedule(schedule.name,day +' ' +schedule.start, day +' ' +schedule.end)
                )

        for schedule in self.schedule_list:
            printing_schedule_list.append(schedule)

        printing_schedule_list.sort()

        for idx, schedule in enumerate(printing_schedule_list) :
            result += str(schedule) + '\n'
            if idx == 9:
                break

        return result.strip()
            
    def _convert_daily_time_to_int(self, time):
        hour = list(map(int, time.split(":")))
        hour = hour[0]*100 + hour[1]

        return hour

    def _check_daily_time(self, time):
        # time type : "09:35"
        target_time = self._convert_daily_time_to_int(time)

        # check ordinary schedule
        for schedule in self.schedule_list:
            _, start_time = self._convert_time_to_int(schedule.start)
            _, end_time = self._convert_time_to_int(schedule.end)

            if start_time < target_time and target_time <= end_time:
                return schedule
        
        # check daily schedule
        for schedule in self.daily_schedule :
            start_time = self._convert_daily_time_to_int(schedule.start)
            end_time = self._convert_daily_time_to_int(schedule.end)

            if start_time < target_time and target_time <= end_time:
                return schedule
        
        return None
    
    def add_schedule(self, name, start, end):
        if self._check_daily_time(start.split()[1]) == None and self._check_daily_time(end.split()[1]) == None:
            super().add_schedule(name, start, end)
        else:
            raise ValueError

    def add_daily_schedule(self, name, start, end):
        if self._check_daily_time(start) == None and self._check_daily_time(end) == None:
            self.daily_schedule.append(Schedule(name, start, end))
        else:
            raise ValueError

    def remove_schedule(self, time):
        if len(time.split()) == 2:
            # time type : "2021-04-05 09:35" , 
            schedule = self._check_time(time)

            if schedule is not None:
                self.schedule_list.remove(schedule)

            # check daily schedule
            _, target_time = self._convert_time_to_int(time)

            for schedule in self.daily_schedule :
                start_time = self._convert_daily_time_to_int(schedule.start)
                end_time = self._convert_daily_time_to_int(schedule.end)

                if start_time < target_time and target_time <= end_time:
                     self.daily_schedule.remove(schedule)
                     return
        else:
            # time type : "09:35"
            schedule = _check_daily_time(time)
            if schedule is not None:
                if len(schedule.start.split()) == 2:
                    self.schedule_list.remove(schedule)
                else:
                    self.daily_schedule.remove(schedule)

    def check_schedule(self, time):
        if len(time.split()) == 2:
            # time type : "2021-04-05 09:35" 
            schedule = self._check_time(time)
            day, hour = time.split()

            if schedule is not None:
                return str(schedule)

            # check daily schedule
            _, target_time = self._convert_time_to_int(time)

            for schedule in self.daily_schedule :
                start_time = self._convert_daily_time_to_int(schedule.start)
                end_time = self._convert_daily_time_to_int(schedule.end)

                if start_time < target_time and target_time <= end_time:
                     return str(Schedule(schedule.name,
                         day + ' ' + schedule.start, day + ' ' + schedule.end))
        else:
            # time type : "09:35"
            schedule = _check_daily_time(time)
            if schedule is not None:
                if len(schedule.start.split()) == 2:
                    return str(schedule)
                else:
                    return str(schedule)

        return ""


if __name__=='__main__':
    calendar = SmartCalendar()
    calendar.add_schedule('Lab meeting', '2021-04-05 13:00','2021-04-05 14:00')
    calendar.add_schedule('Play video game', '2021-04-10 15:00', '2021-04-10 16:00')
    calendar.add_daily_schedule('Breakfast', '08:00', '08:30')
    calendar.add_daily_schedule('Lunch', '12:00', '13:00')
    calendar.add_daily_schedule('Dinner', '18:00', '19:00')
    print(calendar)

    calendar.remove_schedule('2021-04-10 12:30')
    print(calendar)

    try :
        calendar.add_schedule('Homework', '2021-04-06 18:30','2021-04-06 18:45')
    except:
        print("We have another schedule!")

    try :
        calendar.add_daily_schedule('Coffe break', '18:30','18:45')
    except:
        print("We have another schedule!")

    try :
        calendar.add_daily_schedule('Coffe break', '13:30','13:45')
    except:
        print("We have another schedule!")

    print(calendar.check_schedule('2050-12-25 08:15'))
