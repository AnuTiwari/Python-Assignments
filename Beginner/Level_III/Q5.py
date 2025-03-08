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

def main():
    # Taking input from the user for the first time object
    h1 = int(input("Enter hours for first time: "))
    m1 = int(input("Enter minutes for first time: "))
    t1 = Time(h1, m1)

    # Taking input from the user for the second time object
    h2 = int(input("Enter hours for second time: "))
    m2 = int(input("Enter minutes for second time: "))
    t2 = Time(h2, m2)

    # Adding both time objects
    t3 = t1.addTime(t2)

    # Displaying results
    print("\nSum of time:")
    t3.displayTime()
    t3.displayMinute()

if __name__ == "__main__":
    main()