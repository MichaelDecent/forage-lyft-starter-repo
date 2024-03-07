#!/usr/bin/python3
"""
This Module define the class Servicable
"""
from abc import ABC, abstractmethod


class Serviceable(ABC):
    """Cars are accessed through this Seriviable Interface"""

    @abstractmethod
    def needs_service() -> bool:
        """this checks if a car needs servicing"""
        pass
