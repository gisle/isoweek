import sys
import unittest
from isoweek import Week

class TestWeek(unittest.TestCase):
    def test_constructors(self):
        w = Week(2011,1)
        self.assertTrue(w)
        self.assertEqual(str(w), "2011W01")

        w = Week(2011,0)
        self.assertEqual(str(w), "2010W52")
        w = Week(2011,-1)
        self.assertEqual(str(w), "2010W51")

        w = Week(2011,52)
        self.assertEqual(str(w), "2011W52")
        w = Week(2011,53)
        self.assertEqual(str(w), "2012W01")
        w = Week(2011,54)
        self.assertEqual(str(w), "2012W02")

        w = Week(2009,51)
        self.assertEqual(str(w), "2009W51")
        w = Week(2009,52)
        self.assertEqual(str(w), "2009W52")
        w = Week(2009,53)
        self.assertEqual(str(w), "2009W53")
        w = Week(2009,54)
        self.assertEqual(str(w), "2010W01")

        w = Week.thisweek()
        self.assertTrue(w)

        w = Week.fromordinal(1)
        self.assertEqual(str(w), "0001W01")
        w = Week.fromordinal(2)
        self.assertEqual(str(w), "0001W02")
        w = Week.fromordinal(521723)
        self.assertEqual(str(w), "9999W52")

        w = Week.fromstring("2011W01")
        self.assertEqual(str(w), "2011W01")
        w = Week.fromstring("2011-W01")
        self.assertEqual(str(w), "2011W01")

        from datetime import date
        w = Week.withdate(date(2011, 5, 17))
        self.assertEqual(str(w), "2011W20")

        weeks = list(Week.weeks_of_year(2009))
        self.assertEqual(len(weeks), 53)
        self.assertEqual(weeks[0], Week(2009,1))
        self.assertEqual(weeks[-1], Week(2009,53))

        weeks = list(Week.weeks_of_year(2011))
        self.assertEqual(len(weeks), 52)
        self.assertEqual(weeks[0], Week(2011,1))
        self.assertEqual(weeks[-1], Week(2011,52))

        self.assertEqual(Week.last_week_of_year(2009), Week(2009, 53))
        self.assertEqual(Week.last_week_of_year(2010), Week(2010, 52))
        self.assertEqual(Week.last_week_of_year(2011), Week(2011, 52))
        self.assertEqual(Week.last_week_of_year(9999), Week(9999, 52))

        self.assertRaises(ValueError, lambda: Week(0, 0))
        self.assertRaises(ValueError, lambda: Week.fromstring("0000W00"))
        self.assertRaises(ValueError, lambda: Week.fromstring("foo"))
        self.assertRaises(ValueError, lambda: Week.fromordinal(-1))
        self.assertRaises(ValueError, lambda: Week.fromordinal(0))
        self.assertRaises(ValueError, lambda: Week.fromordinal(521724))
        self.assertRaises(ValueError, lambda: Week.last_week_of_year(0))
        self.assertRaises(ValueError, lambda: Week.last_week_of_year(10000))

    def test_mix_max(self):
        self.assertEqual(Week.min, Week(1,1))
        self.assertEqual(Week.max, Week(9999,52))
        self.assertEqual(Week.resolution.days, 7)

        self.assertRaises(ValueError, lambda: Week.min - 1)
        self.assertRaises(ValueError, lambda: Week.max + 1)

    def test_stringification(self):
        w = Week(2011, 20)
        self.assertEqual(str(w), "2011W20")
        self.assertEqual(w.isoformat(), "2011W20")
        self.assertEqual(repr(w), "isoweek.Week(2011, 20)")

    def test_replace(self):
        w = Week(2011, 20)
        self.assertEqual(w.replace(), w)
        self.assertEqual(w.replace(year=2010), Week(2010, 20))
        self.assertEqual(w.replace(week=2), Week(2011, 2))
        self.assertEqual(w.replace(week=99), Week(2012, 47))
        self.assertEqual(w.replace(year=1, week=1), Week(1, 1))

    def test_days(self):
        w = Week(2011, 20)
        self.assertEqual(w.monday().isoformat(),    "2011-05-16")
        self.assertEqual(w.tuesday().isoformat(),   "2011-05-17")
        self.assertEqual(w.wednesday().isoformat(), "2011-05-18")
        self.assertEqual(w.thursday().isoformat(),  "2011-05-19")
        self.assertEqual(w.friday().isoformat(),    "2011-05-20")
        self.assertEqual(w.saturday().isoformat(),  "2011-05-21")
        self.assertEqual(w.sunday().isoformat(),    "2011-05-22")

        self.assertEqual(w.day(0).isoformat(),  "2011-05-16")
        self.assertEqual(w.day(-1).isoformat(), "2011-05-15")
        self.assertEqual(w.day(10).isoformat(), "2011-05-26")

        days = w.days()
        self.assertEqual(len(days), 7)
        self.assertEqual(days[0].isoformat(), "2011-05-16")
        self.assertEqual(days[-1].isoformat(), "2011-05-22")

        from datetime import date
        self.assertFalse(w.contains(date(2011,5,15)))
        self.assertTrue(w.contains(date(2011,5,16)))
        self.assertTrue(w.contains(date(2011,5,22)))
        self.assertFalse(w.contains(date(2011,5,23)))

    def test_arithmetics(self):
        w = Week(2011, 20)
        self.assertEqual(str(w + 0),   "2011W20")
        self.assertEqual(str(w + 1),   "2011W21")
        self.assertEqual(str(w - 1),   "2011W19")
        if sys.version < '3':
            self.assertEqual(str(w + long(1)),  "2011W21")
            self.assertEqual(str(w - long(1)),  "2011W19")
        self.assertEqual(str(w + 52),  "2012W20")
        self.assertEqual(str(w - 104), "2009W21")

        self.assertEqual(w - w, 0)
        self.assertEqual(w - Week(2011, 1), 19)
        self.assertEqual(Week(2011, 1) - w, -19)

        self.assertEqual(str(w + Week.resolution),   "2011W21")
        self.assertEqual(str(w - Week.resolution),   "2011W19")

    def test_arithmetics_subclass(self):
        class MyWeek(Week):
            pass
        w = MyWeek(2011, 20)
        next_week = w + 1
        self.assertEqual(str(next_week),   "2011W21")
        self.assertTrue(isinstance(next_week, MyWeek))

if __name__ == '__main__':
    unittest.main()
