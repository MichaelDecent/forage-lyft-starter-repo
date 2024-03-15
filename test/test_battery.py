import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestBattery(unittest.TestCase):
    def setUp(self):
        """Set up common attributes."""
        self.current_date = datetime.today().date()


class TestNubbinBattery(TestBattery):
    """Test cases for the Nubbin Battery"""

    def test_battery_should_be_service(self):
        """Test if Nubbin battery needs service."""
        last_service_date1 = self.current_date.replace(year=self.current_date.year - 4)

        last_service_date2 = self.current_date.replace(year=self.current_date.year - 6)

        battery1 = NubbinBattery(last_service_date1, self.current_date)
        self.assertTrue(battery1.needs_service())

        battery2 = NubbinBattery(last_service_date2, self.current_date)
        self.assertTrue(battery2.needs_service())

    def test_battery_should_be_not_service(self):
        """Test if Nubbin battery does not need service."""

        last_service_date1 = self.current_date.replace(year=self.current_date.year - 2)

        last_service_date2 = self.current_date.replace(year=self.current_date.year - 0)

        battery1 = NubbinBattery(last_service_date1, self.current_date)
        self.assertFalse(battery1.needs_service())

        battery2 = NubbinBattery(last_service_date2, self.current_date)
        self.assertFalse(battery2.needs_service())


class TestSpindlerBattery(TestBattery):
    """Test cases for the Spindler Battery"""

    def test_battery_should_be_service(self):
        """Test if Spindler battery needs service."""

        last_service_date1 = self.current_date.replace(year=self.current_date.year - 3)

        last_service_date2 = self.current_date.replace(year=self.current_date.year - 6)

        battery1 = SpindlerBattery(last_service_date2, self.current_date)
        self.assertTrue(battery1.needs_service())

        battery2 = SpindlerBattery(last_service_date1, self.current_date)
        self.assertTrue(battery2.needs_service())

    def test_battery_should_be_not_service(self):
        """Test if Spindler battery does not need service."""
        last_service_date1 = self.current_date.replace(year=self.current_date.year - 0)

        last_service_date2 = self.current_date.replace(year=self.current_date.year - 2)

        battery1 = SpindlerBattery(last_service_date1, self.current_date)
        self.assertFalse(battery1.needs_service())

        battery2 = SpindlerBattery(last_service_date2, self.current_date)
        self.assertFalse(battery2.needs_service())


if __name__ == "__main__":
    unittest.main()
