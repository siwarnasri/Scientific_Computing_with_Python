import unittest
from time_calculator import add_time


class UnitTests(unittest.TestCase):

    def test_same_period(self):
        print("# Testing add_time('3:30 PM', '2:12'), expected = '5:42 PM'", "\n")
        print("Return:", add_time("3:30 PM", "2:12"), "\n", "\n") 
      
    def test_different_period(self):
        print("# Testing add_time('11:55 AM', '3:12'), expected = '3:07 PM'", "\n")
        print("Return:", add_time("11:55 AM", "3:12"), "\n", "\n")

    def test_am_pm_error(self):
        print("# Testing add_time('11:55 M', '3:12'), expected = 'Error'", "\n")
        print("Return:", add_time("11:55 M", "3:12"), "\n", "\n")

    def test_int_error(self):
        print("# Testing add_time('141:55 AM', '3:12'), expected = 'Error'", "\n")
        print("Return:", add_time("141:55 AM", "3:12"), "\n", "\n")

    def test_int_error(self):
        print("# Testing add_time('11:95 AM', '3:12'), expected = 'Error'", "\n")
        print("Return:", add_time("11:95 AM", "3:12"), "\n", "\n")

    def test_DAY_error(self):
        print("# Testing add_time('11:55 AM', '3:12', 'day_x'), expected = 'Error'", "\n")
        print("Return:", add_time("11:55 AM", "3:12", 'day_x'), "\n", "\n")
      
    def test_next_day(self):
        print("# Testing add_time('9:15 PM', '5:30'), expected = '2:45 AM (next day)'", "\n")
        print("Return:", add_time("9:15 PM", "5:30"), "\n", "\n")
      
    def test_period_change_at_twelve(self):
        print("# Testing add_time('11:40 AM', '0:25'), expected = '0:05 PM'", "\n")
        print("Return:", add_time("11:40 AM", "0:25"), "\n", "\n")
      
    def test_twenty_four(self):
        print("# Testing add_time('2:59 AM', '2:12'), expected = '5:11 AM'", "\n")
        print("Return:", add_time("2:59 AM", "2:12"), "\n", "\n")
       
    def test_two_days_later(self):
        print("# Testing add_time('11:59 PM', '24:05'), expected = '0:04 AM (2 days later)'", "\n")
        print("Return:", add_time("11:59 PM", "24:05"), "\n", "\n")
      
    def test_high_duration(self):
        print("# Testing add_time('8:16 PM', '466:02'), expected = '6:18 AM (20 days later)'", "\n")
        print("Return:", add_time("8:16 PM", "466:02"), "\n", "\n")

    def test_no_change(self):
        print("# Testing add_time('5:01 AM', '0:00'), expected = '5:01 AM'", "\n")
        print("Return:", add_time("5:01 AM", "0:00"), "\n", "\n")
        
    def test_same_period_with_day(self):
        print("# Testing add_time('3:30 PM', '2:12', 'Monday', expected = '5:42 PM, Monday')", "\n")
        print("Return:", add_time("3:30 PM", "2:12", "Monday"), "\n", "\n")
        
    def test_twenty_four_with_day(self):
        print("# Testing add_time('2:59 AM', '24:00', 'saturDay', expected = '2:59 AM, Sunday (next day)')", "\n")
        print("Return:", add_time("2:59 AM", "24:00", "saturDay"), "\n", "\n")
      
    def test_two_days_later_with_day(self):
        print("# Testing add_time('11:59 PM', '24:05', 'Wednesday', expected = '0:04 AM, Friday (2 days later)')", "\n")
        print("Return:", add_time('11:59 PM', '24:05', 'Wednesday'), "\n", "\n")
      
    def test_high_duration_with_day(self):
        print("# Testing add_time('8:16 PM', '466:02', 'tuesday', expected = '6:18 AM, Monday (20 days later)')", "\n")
        print("Return:", add_time('8:16 PM', '466:02', 'tuesday'), "\n", "\n")


      

if __name__ == "__main__":
    unittest.main()