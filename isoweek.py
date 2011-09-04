from datetime import date, timedelta

class Week(object):
    __slots__ = ('year', 'week')

    def __init__(self, *args):
        if len(args) == 1:
            o = args[0]
            if isinstance(o, Week):
                self.year = o.year
                self.week = o.week
            elif isinstance(o, str) and len(o) == 7 and o[4] == 'W':
                self.year = int(o[0:4])
                self.week = int(o[5:7])
                self.normalize()
            elif isinstance(o, date):
                self.year, self.week, weekday = o.isocalendar()
            elif isinstance(o, int):
                self.year, self.week, weekday = date.fromordinal(o * 7 + 1).isocalendar()
            else:
                raise ValueError("Bad isoweek.Week constructor")
        elif len(args) == 2:
            self.year, self.week = args
            self.normalize()
        elif len(args) == 0:
            self.year, self.week, weekday = date.today().isocalendar()
        else:
            raise ValueError("Bad isoweek.Week constructor")

    def day(self, num):
        d = date(self.year, 1, 4)  # The Jan 4th must be in week 1 according to ISO
        return d + timedelta(weeks=self.week-1, days=-d.weekday() + num)

    def monday(self):
        return self.day(0)

    def toordinal(self):
        return self.monday().toordinal() / 7

    def inc(self, increment=1):
        self.week += increment
        self.normalize()
        return self

    def normalize(self):
        w = Week(self.toordinal())
        self.year = w.year
        self.week = w.week

    def year_week(self):
        return self.year, self.week

    def __repr__(self):
        return "%04dW%02d" % (self.year, self.week)

    def __add__(self, other):
        w = Week(self)
        w.inc(other)
        return w

    def __sub__(self, other):
        return self.toordinal() - other.toordinal()

    def __iadd__(self, other):
        return self.inc(other)

    def __isub__(self, other):
        return self.inc(-other)

if __name__ == '__main__':
    w = Week(2011, 99)
    print w
    print str(w)
    print w.year
    print w.week
    print w.monday()
    print w.toordinal()

    w = Week()
    print w
    w.inc()
    print w + 1
    print w - Week()
