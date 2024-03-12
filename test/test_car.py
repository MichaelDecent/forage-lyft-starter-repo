import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.sternman_engine import SternmanEngine
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from car import Car


class CarSetup(unittest.TestCase):
    def setUp(self):
        self.current_date = datetime.today()


class TestCarFactory(CarSetup, unittest.TestCase):
    """Test cases for CarFactory"""

    def test_create_calliope(self):
        """Test the creation of Calliope car."""
        last_service_date = self.current_date.replace(year=self.current_date.year - 4)
        current_mileage = 20000
        last_service_mileage = 100000

        calliope_car = Car(
            CapuletEngine(current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date, self.current_date),
        )

        self.assertIsInstance(calliope_car.engine, CapuletEngine)
        self.assertIsInstance(calliope_car.battery, SpindlerBattery)

    def test_calliope_car_needs_service(self):
        """Test if Calliope car needs service."""
        last_service_date = self.current_date.replace(year=self.current_date.year - 4)
        current_mileage = 60000
        last_service_mileage = 10000

        calliope_car = Car(
            CapuletEngine(current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date, self.current_date),
        )
        self.assertTrue(calliope_car.needs_service())

    def test_calliope_car_does_not_need_service(self):
        """Test if Calliope car does not need service."""
        last_service_date = self.current_date.replace(year=self.current_date.year - 1)
        current_mileage = 30000
        last_service_mileage = 10000

        calliope_car = Car(
            CapuletEngine(current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date, self.current_date),
        )

        self.assertFalse(calliope_car.needs_service())

    def test_create_glissade(self):
        """Test the creation of Glissade car."""
        last_service_date = self.current_date.replace(year=self.current_date.year - 4)
        current_mileage = 20000
        last_service_mileage = 100000

        glissade_car = Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date, self.current_date),
        )

        self.assertIsInstance(glissade_car.engine, WilloughbyEngine)
        self.assertIsInstance(glissade_car.battery, SpindlerBattery)

    def test_glissade_car_needs_service(self):
        """Test if Glissade car needs service."""
        last_service_date = self.current_date.replace(year=self.current_date.year - 4)
        current_mileage = 60000
        last_service_mileage = 10000

        glissade_car = Car(
            CapuletEngine(current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date, self.current_date),
        )
        self.assertTrue(glissade_car.needs_service())

    def test_glissade_car_does_not_need_service(self):
        """Test if Glissade car does not need service."""
        last_service_date = self.current_date.replace(year=self.current_date.year - 1)
        current_mileage = 30000
        last_service_mileage = 10000

        glissade_car = Car(
            CapuletEngine(current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date, self.current_date),
        )

        self.assertFalse(glissade_car.needs_service())

    def test_create_palindrome(self):
        """Test the creation of Palindrome car."""
        last_service_date = self.current_date.replace(year=self.current_date.year - 4)
        warning_light_on = True

        palindrome_car = Car(
            SternmanEngine(warning_light_on),
            SpindlerBattery(last_service_date, self.current_date),
        )

        self.assertIsInstance(palindrome_car.engine, SternmanEngine)
        self.assertIsInstance(palindrome_car.battery, SpindlerBattery)

    def test_palindrome_car_needs_service(self):
        """Test if Palindrome car needs service."""
        last_service_date = self.current_date.replace(year=self.current_date.year - 4)
        warning_light_on = True

        palindrome_car = Car(
            SternmanEngine(warning_light_on),
            SpindlerBattery(last_service_date, self.current_date),
        )
        self.assertTrue(palindrome_car.needs_service())

    def test_palindrome_car_does_not_need_service(self):
        """Test if Palindrome car does not need service."""
        last_service_date = self.current_date.replace(year=self.current_date.year - 1)
        warning_light_on = False

        palindrome_car = Car(
            SternmanEngine(warning_light_on),
            SpindlerBattery(last_service_date, self.current_date),
        )

        self.assertFalse(palindrome_car.needs_service())

    def test_create_rorschach(self):
        """Test the creation of Rorschach car."""
        last_service_date = self.current_date.replace(year=self.current_date.year - 4)
        current_mileage = 60000
        last_service_mileage = 10000

        rorschach_car = Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            NubbinBattery(last_service_date, self.current_date),
        )

        self.assertIsInstance(rorschach_car.engine, WilloughbyEngine)
        self.assertIsInstance(rorschach_car.battery, NubbinBattery)

    def test_rorschach_car_needs_service(self):
        """Test if Rorschach car needs service."""
        last_service_date = self.current_date.replace(year=self.current_date.year - 4)
        current_mileage = 60000
        last_service_mileage = 10000

        rorschach_car = Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            NubbinBattery(last_service_date, self.current_date),
        )
        self.assertTrue(rorschach_car.needs_service())

    def test_rorschach_car_does_not_need_service(self):
        """Test if Rorschach car does not need service."""
        last_service_date = self.current_date.replace(year=self.current_date.year - 1)
        current_mileage = 30000
        last_service_mileage = 10000

        rorschach_car = Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            NubbinBattery(last_service_date, self.current_date),
        )

        self.assertFalse(rorschach_car.needs_service())

    def test_create_thovex(self):
        """Test the creation of Thovex car."""
        last_service_date = self.current_date.replace(year=self.current_date.year - 4)
        current_mileage = 60000
        last_service_mileage = 10000

        thovex_car = Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            NubbinBattery(last_service_date, self.current_date),
        )

        self.assertIsInstance(thovex_car.engine, WilloughbyEngine)
        self.assertIsInstance(thovex_car.battery, NubbinBattery)

    def test_thovex_car_should_need_service(self):
        """Test if thovex car does need service."""

        last_service_date = self.current_date.replace(year=self.current_date.year - 4)
        current_mileage = 60000
        last_service_mileage = 10000

        thovex_car = Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            NubbinBattery(last_service_date, self.current_date),
        )
        self.assertTrue(thovex_car.needs_service())

    def test_thovex_car_should_not_need__service(self):
        """Test if thovex car does not need service."""

        last_service_date = self.current_date.replace(year=self.current_date.year - 1)
        current_mileage = 30000
        last_service_mileage = 10000

        thovex_car = Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            NubbinBattery(last_service_date, self.current_date),
        )

        self.assertFalse(thovex_car.needs_service())
