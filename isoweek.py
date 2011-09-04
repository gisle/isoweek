from datetime import date, timedelta
from collections import namedtuple

class Week(namedtuple('Week', ('year', 'week'))):
    """A Week represents a period of 7 days starting with a Monday.
    """
    __slots__ = ()

    @classmethod
    def thisweek(cls):
        return cls(*(date.today().isocalendar()[:2]))

    @classmethod
    def fromordinal(cls, ordinal):
        return cls(*(date.fromordinal(ordinal * 7 + 1).isocalendar()[:2]))

    @classmethod
    def fromstring(cls, isostring):
        if isinstance(isostring, str) and len(isostring) == 7 and isostring[4] == 'W':
           return cls(int(isostring[0:4]), int(isostring[5:7]))
        else:
            raise ValueError("Week.tostring argument must be on the form <yyyy>W<ww>")

    def day(self, num):
        d = date(self.year, 1, 4)  # The Jan 4th must be in week 1 according to ISO
        return d + timedelta(weeks=self.week-1, days=-d.weekday() + num)

    def monday(self):
        return self.day(0)

    def toordinal(self):
        return self.monday().toordinal() / 7

    def normalize(self):
        w = Week(self.toordinal())
        self.year = w.year
        self.week = w.week

    def year_week(self):
        return self.year, self.week

    def __str__(self):
        return "%04dW%02d" % (self.year, self.week)

    def __repr__(self):
        return "Week(%d,%d)" % (self.year, self.week)

    def __add__(self, other):
        return Week.fromordinal(self.toordinal() + other)

    def __sub__(self, other):
        if isinstance(other, int):
            return self.__add__(-other)
        return self.toordinal() - other.toordinal()

if __name__ == '__main__':
    w = Week(2011, 99)
    print w
    print str(w)
    print w.year
    print w.week
    print w.monday()
    print w.toordinal()

    w = Week.thisweek()
    print w
    print w + 1
    print w - 1
    print w - (Week.thisweek() + 3)

    d = {}
    d[Week.thisweek()] = "this week"
    print d[Week.thisweek()]
    print d

    print Week.fromstring("2011W01") < Week.fromstring("2011W02")
    print Week.fromstring("2011W01") != Week.fromstring("2011W02")
    print Week.fromstring("2010W01") < Week.fromstring("2011W01")
