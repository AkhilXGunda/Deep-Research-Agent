"""
Report Writer Agent - Generates comprehensive research reports
"""

from pydantic import BaseModel, Field
from agents import Agent

from .base_agent import BaseAgent


class ResearchReport(BaseModel):
    """Comprehensive research report with multiple components."""
    executive_summary: str = Field(
        description="A concise 2-3 sentence summary of the key findings and conclusions"
    )
    markdown_content: str = Field(
        description="The complete research report in markdown format, 5-10 pages (1000+ words)"
    )
    future_research_directions: list[str] = Field(
        description="Suggested topics and questions for follow-up research"
    )


class ReportWriter(BaseAgent):
    """
    Agent responsible for creating comprehensive research reports.
    Synthesizes research data into well-structured, detailed reports.
    """

    def __init__(self):
        super().__init__()
        self.agent = self._create_agent()

    def _create_agent(self) -> Agent:
        """Create the report writing agent."""
        instructions = """
        You are a senior research analyst and report writer with expertise in creating 
        comprehensive, well-structured research reports.
        
        Your process:
        1. **Analysis Phase**: Thoroughly analyze the research query and collected data
        2. **Outline Creation**: Develop a logical structure and flow for the report
        3. **Content Generation**: Write a detailed, comprehensive report (5-10 pages, 1000+ words)
        4. **Quality Assurance**: Ensure accuracy, clarity, and professional presentation
        
        Report Structure:
        - Executive Summary: Key findings and conclusions
        - Introduction: Research context and objectives
        - Methodology: Approach to data collection and analysis
        - Findings: Detailed analysis of research results
        - Discussion: Interpretation and implications
        - Conclusions: Summary of key insights
        - Future Research: Suggested follow-up investigations
        
        Writing Guidelines:
        - Use clear, professional language
        - Include relevant data, statistics, and examples
        - Maintain logical flow and coherence
        - Cite sources appropriately
        - Balance depth with readability
        - Ensure factual accuracy and objectivity
        """
        
        return Agent(
            name="Research Report Writer",
            instructions=instructions,
            model="gpt-4o-mini",
            output_type=ResearchReport,
        )
