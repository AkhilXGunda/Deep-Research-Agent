"""
Web Researcher Agent - Performs web searches and summarizes findings
"""

from agents import Agent, WebSearchTool, ModelSettings

from .base_agent import BaseAgent


class WebResearcher(BaseAgent):
    """
    Agent responsible for performing web searches and creating concise summaries.
    Focuses on extracting key information from search results.
    """

    def __init__(self):
        super().__init__()
        self.agent = self._create_agent()

    def _create_agent(self) -> Agent:
        """Create the web research agent."""
        instructions = """
        You are a skilled research analyst specializing in web search and information synthesis.
        
        Your task is to:
        1. Perform web searches for the given search terms
        2. Analyze and synthesize the search results
        3. Create concise, factual summaries (2-3 paragraphs, under 300 words)
        4. Focus on key insights, facts, and data points
        5. Eliminate fluff and unnecessary details
        6. Write in a clear, objective tone suitable for further analysis
        
        Important guidelines:
        - Prioritize accuracy and relevance over completeness
        - Capture the essence of findings without verbose explanations
        - Use bullet points or concise sentences when appropriate
        - Focus on recent, authoritative sources
        - Avoid speculation or personal opinions
        - Ensure summaries are ready for integration into larger reports
        """
        
        return Agent(
            name="Web Research Analyst",
            instructions=instructions,
            tools=[WebSearchTool(search_context_size="low")],
            model="gpt-4o-mini",
            model_settings=ModelSettings(tool_choice="required"),
        )
