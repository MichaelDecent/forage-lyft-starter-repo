#!/usr/bin/env python3
"""This Module describes the WilloughbyEngine class"""
from engine.engine_interface import Engine


class WilloughbyEngine(Engine):
    """This class defines the criteria for CapuletEngine"""

    def __init__(self, current_millage: int, last_service_millage: int) -> None:
        self.current_millage = current_millage
        self.last_service_millage = last_service_millage

    def needs_service(self) -> bool:
        """this determins if the willoughby engine needs servicing"""
        return self.current_mileage - self.last_service_mileage > 60000
