#!/usr/bin/env python3

""" this Module describes the Tire Class"""
from abc import ABC, abstractmethod


class Tire(ABC):
    """This class define an interface for different tires"""

    @abstractmethod
    def needs_service() -> bool:
        """This is an abstarct method that returns a boolean value"""
        pass
