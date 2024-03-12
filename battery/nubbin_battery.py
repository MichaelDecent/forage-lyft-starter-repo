#!/usr/bin/env python3
"""This Module describes the NubbinBattery class"""
from battery.battery_interface import Battery
from datetime import datetime


class NubbinBattery(Battery):
    """This class defines the criteria for NubbinBattery"""

    def __init__(self, last_service_date: datetime, current_date: datetime) -> None:
        self.service_threshold_date = last_service_date.replace(year=last_service_date.year + 4)
        self.current_date = current_date

    def needs_service(self) -> bool:
        """This determines if the nubbin battery needs servicing"""
        return self.current_date >= self.service_threshold_date 
