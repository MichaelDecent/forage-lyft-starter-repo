#!/usr/bin/python3
"""This Module describes the CarFactory Class and its methods"""
from datetime import datetime
from car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory(Car):
    """This class defines methods for creating a car model"""

    @staticmethod
    def create_calliope(
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        """this helps to create the calliope car model"""
        return Car(
            CapuletEngine(current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date, current_date),
        )

    @staticmethod
    def create_glissade(
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        """this helps to create the glissade car model"""
        return Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date, current_date),
        )

    @staticmethod
    def create_palindrome(
        current_date: datetime, last_service_date: datetime, warning_light_no: bool
    ) -> Car:
        """this helps to create the palidrome car model"""
        return Car(
            SternmanEngine(warning_light_no),
            SpindlerBattery(last_service_date, current_date),
        )

    @staticmethod
    def create_rorschach(
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        """this helps to create the rorschach car model"""
        return Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            NubbinBattery(last_service_date, current_date),
        )

    @staticmethod
    def create_thovex(
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        """this helps to create the thovex car model"""
        return Car(
            CapuletEngine(current_mileage, last_service_mileage),
            NubbinBattery(last_service_date, current_date),
        )
