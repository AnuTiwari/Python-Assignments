class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, t):
        total_minutes = self.minutes + t.minutes
        total_hours = self.hours + t.hours + (total_minutes // 60)
        total_minutes %= 60
        return Time(total_hours, total_minutes)

    def displayTime(self):
        print(f"{self.hours} hr {self.minutes} min")

    def displayMinute(self):
        print(f"Total minutes: {self.hours * 60 + self.minutes}")

t1 = Time(2, 50)
t2 = Time(1, 20)
t3 = t1.addTime(t2)
t3.displayTime()
t3.displayMinute()
