#!/usr/bin/env python3
"""This Module describes the OctoprimeTire class"""
from .tire_interface import Tire
from typing import List


class OctoprimeTire(Tire):
    """This class defines the criteria for OctoprimeTire"""

    def __init__(self, wear_sensors: List[float]) -> None:
        self.wear_sensors = wear_sensors

    def needs_service(self) -> bool:
        """This determines if the octoprime tire needs servicing"""

        return sum(self.wear_sensors) >= 3
