#!/usr/bin/env python3
"""This Module describes the CarriganTire class"""
from .tire_interface import Tire
from typing import List


class CarriganTire(Tire):
    """This class defines the criteria for CarriganTire"""

    def __init__(self, wear_sensors: List[float]) -> None:
        self.wear_sensors = wear_sensors

    def needs_service(self) -> bool:
        """This determines if the carrigan tire needs servicing"""
        for val in self.wear_sensors:
            if val >= 0.9:
                return True
        return False
