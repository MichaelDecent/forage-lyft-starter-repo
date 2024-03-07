#!/usr/bin/env python3
"""This Module describes the Engine Class"""
from abc import ABC, abstractmethod

class Engine(ABC):
    """This class define an interface for different engine"""

    @abstractmethod
    def needs_service() -> bool:
        """This is an abstarct method that returns a boolean value"""
        pass
