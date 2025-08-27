"""
Report Formatter - Formats research reports for display
"""

from agents import Agent

from .base_agent import BaseAgent


class ReportFormatter(BaseAgent):
    """
    Agent responsible for formatting research reports for display.
    Focuses on creating well-structured, readable content.
    """

    def __init__(self):
        super().__init__()
        self.agent = self._create_agent()

    def _create_agent(self) -> Agent:
        """Create the report formatting agent."""
        instructions = """
        You are a professional content formatter specializing in research reports. 
        Your task is to ensure research reports are well-structured, readable, and 
        professionally presented for display in a web interface.
        
        Guidelines:
        1. Ensure proper markdown formatting and structure
        2. Improve readability with clear headings and sections
        3. Add appropriate formatting for lists, tables, and code blocks
        4. Maintain professional tone and presentation
        5. Make content accessible and easy to scan
        6. Ensure consistent formatting throughout the report
        
        Focus on:
        - Clear section headers and subheaders
        - Proper use of markdown syntax
        - Logical flow and organization
        - Professional presentation
        - Readability and accessibility
        """
        
        return Agent(
            name="Research Report Formatter",
            instructions=instructions,
            model="gpt-4o-mini",
        )

    def format_report_for_display(self, report_content: str) -> str:
        """
        Format the research report for display in the web interface.
        
        Args:
            report_content: The markdown report content
            
        Returns:
            Formatted report content
        """
        # For now, just return the markdown content as-is
        # In the future, this could add additional formatting or validation
        return report_content
