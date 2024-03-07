#!/usr/bin/env python3
"""This Module describes the SternmanEngine class"""
from engine.engine_interface import Engine


class SternmanEngine(Engine):
    """This class defines the criteria for SternmanEngine"""

    def __init__(self, warning_light_on: bool) -> None:
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        """This determines if the sternman engine needs servicing"""
        return self.warning_light_on
