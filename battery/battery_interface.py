#!/usr/bin/env python3
""" this Module describes the Battery Class"""
from abc import ABC, abstractmethod

class Battery(ABC):
    """This class define an interface for different battery"""

    @abstractmethod
    def needs_service() -> bool:
        """This is an abstarct method that returns a boolean value"""
        pass
