import unittest

from engine.sternman_engine import SternmanEngine
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine


class TestEngine(unittest.TestCase):
    def setUp(self) -> None:
        self.current_mileage1 = 40000
        self.current_mileage2 = 80000
        self.current_mileage3 = 30000
        self.last_service_mileage1 = 10000
        self.last_service_mileage2 = 20000
        self.warning_light_on = True
        self.warning_light_off = False


class TestCapuletEngine(TestEngine, unittest.TestCase):
    """Test cases for the CapuletEngine"""

    def test_engine_should_be_service(self) -> None:
        """test for cases where capulet engine should be serviced"""

        capulet_engine1 = CapuletEngine(
            self.current_mileage1, self.last_service_mileage1
        )
        self.assertTrue(capulet_engine1.needs_service())

        capulet_engine2 = CapuletEngine(
            self.current_mileage2, self.last_service_mileage1
        )
        self.assertTrue(capulet_engine2.needs_service())

    def test_engine_should_be_not_service(self) -> None:
        """test for cases where capulet engine should not be serviced"""

        capulet_engine1 = CapuletEngine(
            self.current_mileage1, self.last_service_mileage2
        )
        self.assertFalse(capulet_engine1.needs_service())

        capulet_engine2 = CapuletEngine(
            self.current_mileage3, self.last_service_mileage2
        )
        self.assertFalse(capulet_engine2.needs_service())


class TestWilloughbyEngine(TestEngine, unittest.TestCase):
    """Test cases for the WilloughbyEngine"""

    def test_engine_should_be_service(self) -> None:
        """test for cases where willoughby engine should be serviced"""

        willoughby_engine1 = WilloughbyEngine(
            self.current_mileage2, self.last_service_mileage1
        )
        self.assertTrue(willoughby_engine1.needs_service())

        willoughby_engine2 = WilloughbyEngine(
            self.current_mileage2, self.last_service_mileage2
        )
        self.assertTrue(willoughby_engine2.needs_service())

    def test_engine_should_be_not_service(self) -> None:
        """test for cases where willoughby engine should not be serviced"""

        willoughby_engine1 = WilloughbyEngine(
            self.current_mileage1, self.last_service_mileage2
        )
        self.assertFalse(willoughby_engine1.needs_service())

        willoughby_engine2 = WilloughbyEngine(
            self.current_mileage3, self.last_service_mileage2
        )
        self.assertFalse(willoughby_engine2.needs_service())


class TestSternmanEngine(TestEngine, unittest.TestCase):
    """Test cases for the SternmanEngine"""

    def test_engine_should_be_service(self) -> None:
        """test for cases where sternman engine should be serviced"""

        sternman_engine = SternmanEngine(self.warning_light_on)
        self.assertTrue(sternman_engine.needs_service())

    def test_engine_should_be_not_service(self) -> None:
        """test for cases where sternman engine should not be serviced"""

        sternman_engine = SternmanEngine(self.warning_light_off)
        self.assertFalse(sternman_engine.needs_service())
