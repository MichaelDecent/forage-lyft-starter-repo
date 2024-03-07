#!/usr/bin/env python3
"""This module defines the class model"""
from abc import ABC
from servicable import Serviceable
from engine.engine_interface import Engine
from battery.battery_interface import Battery


class Car(Serviceable, ABC):
    """This defines a class Model"""

    def __init__(self, engine: Engine, battery: Battery) -> None:
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        """this determines if a car needs servicing"""

        if self.engine.needs_service() or self.battery.needs_service():
            return True
        return False
