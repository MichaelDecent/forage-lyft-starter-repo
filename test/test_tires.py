import unittest

from tires.carrigan_tire import CarriganTire
from tires.octoprime_tire import OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    """Test cases for the CarriganTire"""

    def test_tire_should_be_service(self) -> None:
        """test for cases where carrigan tire should be serviced"""
        wear_sensor = [0.25, 0.5, 0.75, 0.9]

        carrigan_tire = CarriganTire(wear_sensor)

        self.assertTrue(carrigan_tire.needs_service())

    def test_tire_should_not_be_service(self) -> None:
        """test for cases where carrigan tire should not be serviced"""
        wear_sensor = [0.25, 0.5, 0.75, 0.89]

        carrigan_tire = CarriganTire(wear_sensor)

        self.assertFalse(carrigan_tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):
    """Test cases for the OctoprimeTire"""

    def test_tire_should_be_service(self) -> None:
        """test for cases where octoprime tire should be serviced"""
        wear_sensor = [0.5, 0.9, 0.75, 0.9]

        octoprime_tire = OctoprimeTire(wear_sensor)

        self.assertTrue(octoprime_tire.needs_service())

    def test_tire_should_not_be_service(self) -> None:
        """test for cases where octoprime tire should not be serviced"""
        wear_sensor = [0.25, 0.5, 0.75, 0.9]

        octoprime_tire = OctoprimeTire(wear_sensor)

        self.assertFalse(octoprime_tire.needs_service())
