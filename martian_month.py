class MartianMonth(object):
    "帝國火星暦の月"

    def __init__(self, month):
        self.month = month

    def days(self):
        "この月の日數"

        month = self.month
        if month % 6 == 0:
            return 27
        else:
            return 28
