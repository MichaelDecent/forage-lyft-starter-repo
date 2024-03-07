#!/usr/bin/env python3
"""This Module describes the CapuletEngine class"""
from engine.engine_interface import Engine


class CapuletEngine(Engine):
    """This class defines the criteria for CapuletEngine"""

    def __init__(self, current_mileage: int, last_service_mileage: int) -> None:
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        """This determins if the capulet engine needs servicing"""
        return self.current_mileage - self.last_service_mileage > 30000
