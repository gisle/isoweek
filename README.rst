ISO Week
========

The isoweek module provide the class `Week`.  Instances represent specific weeks
spanning Monday to Sunday.  There are 52 or 53 numbered weeks in a year.  Week
1 is defined to be the first week with 4 or more days in January.

It's called isoweek because this is the week definition of ISO 8601.  This
standard also define a notation for identifying weeks; YYYYWww (where the "W"
is a literal).  An example is "2011W20" which denotes the 20th week of year
2011.  `Week` instances stringify to this form.

The `Week` instances are light weight and immutable with an interface similar
to the datetime.date objects.  Example code::

    from isoweek import Week
    w = Week(2011, 20)
    print "Week %s starts on %s" % (w, w.monday().isoformat())

    print "Current week: %d" % (Week.thisweek().week,)
