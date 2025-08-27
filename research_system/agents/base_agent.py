"""
Base Agent Class - Common functionality for all research agents
"""

from abc import ABC, abstractmethod
from agents import Agent


class BaseAgent(ABC):
    """
    Abstract base class for all research agents.
    Provides common functionality and interface.
    """

    def __init__(self):
        self.agent: Agent = None

    @abstractmethod
    def _create_agent(self) -> Agent:
        """Create and configure the specific agent implementation."""
        pass

    def get_agent(self) -> Agent:
        """Get the configured agent instance."""
        return self.agent
