import arrow
from odoo.tests.common import TransactionCase
from datetime import date
from ..dttools import str2datetime, date_range_overlap, remove_times


class TestDates(TransactionCase):
    def test_dates(self):
        d = str2datetime("1980-04-04 23:23:23")
        assert date_range_overlap(
            (date(2013, 4, 4), date(2013, 4, 10)), (date(2013, 4, 5), date(2013, 4, 6))
        )
        assert date_range_overlap(
            (date(2013, 4, 4), date(2013, 4, 10)), (date(2013, 4, 2), date(2013, 4, 12))
        )
        assert date_range_overlap(
            (date(2013, 4, 4), date(2013, 4, 10)), (date(2013, 4, 9), date(2013, 4, 12))
        )
        assert not date_range_overlap(
            (date(2013, 4, 4), date(2013, 4, 10)), (date(2013, 4, 2), date(2013, 4, 3))
        )
        assert date_range_overlap(
            (date(2013, 4, 4), date(2013, 4, 10)), (date(2013, 4, 2), date(2013, 4, 4))
        )
        assert date_range_overlap(
            (date(2013, 4, 4), date(2013, 4, 10)), (date(2013, 4, 2), date(2013, 4, 5))
        )

    def test_remove_times(self):
        tz = "Europe/Berlin"
        start = arrow.get("1980-04-04 08:00:00").replace(tzinfo="utc").datetime
        end = arrow.get("1980-04-04 10:00:00").replace(tzinfo="utc").datetime
        break_start = 9.5
        break_end = 10
        break_timezone = tz

        self.assertEqual(
            remove_times(start, end, [(4, break_start, break_end, break_timezone)]), 90
        )
        self.assertEqual(
            remove_times(start, end, [(3, break_start, break_end, break_timezone)]), 120
        )

        # test with filters
        filters = [
            (
                arrow.get(start).shift(minutes=30).datetime,
                arrow.get(start).shift(minutes=40).datetime,
            )
        ]
        self.assertEqual(
            remove_times(start, end, [], filters=filters),
            10,
        )
