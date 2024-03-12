#!/usr/bin/env python3
"""This Module describes the SpindlerBattery class"""
from battery.battery_interface import Battery
from datetime import datetime


class SpindlerBattery(Battery):
    """This class defines the criteria for SpindlerBattery"""

    def __init__(self, last_service_date: datetime, current_date: datetime) -> None:
        self.service_threshold_date = last_service_date.replace(year=last_service_date.year + 2)
        self.current_date = current_date

    def needs_service(self) -> bool:
        """This determines if the spindler battery needs servicing"""
        return self.current_date >= self.service_threshold_date 
