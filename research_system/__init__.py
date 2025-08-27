"""
Deep Research System - A multi-agent research platform
"""

from .core.research_orchestrator import ResearchOrchestrator
from .agents.search_planner import SearchPlanner
from .agents.web_researcher import WebResearcher
from .agents.report_writer import ReportWriter
from .agents.notification_sender import ReportFormatter

__version__ = "1.0.0"
__all__ = [
    "ResearchOrchestrator",
    "SearchPlanner", 
    "WebResearcher",
    "ReportWriter",
    "ReportFormatter"
]
