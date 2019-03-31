class MartianDateTime(object):
    "帝國火星暦の日時"

    def __init__(self, year, month, day, hour, minute, second):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    def __eq__(self, other):
        if not isinstance(other, MartianDateTime):
            return False
        return self.__dict__ == other.__dict__
