"""
Search Planner Agent - Creates optimized search strategies for research queries
"""

from pydantic import BaseModel, Field
from agents import Agent

from .base_agent import BaseAgent


class SearchQuery(BaseModel):
    """Represents a single search query with its rationale."""
    query: str = Field(description="The specific search term or phrase to query")
    rationale: str = Field(description="Explanation of why this search is important for the research")


class SearchStrategy(BaseModel):
    """Complete search strategy containing multiple targeted queries."""
    search_queries: list[SearchQuery] = Field(
        description="List of strategic search queries to comprehensively answer the research question",
        min_items=3,
        max_items=7
    )


class SearchPlanner(BaseAgent):
    """
    Agent responsible for creating comprehensive search strategies.
    Analyzes research queries and generates optimal search terms.
    """

    def __init__(self):
        super().__init__()
        self.agent = self._create_agent()

    def _create_agent(self) -> Agent:
        """Create the search planning agent."""
        instructions = """
        You are an expert research strategist. Given a research query, you create a comprehensive 
        search strategy to gather the most relevant and diverse information.
        
        Your task is to:
        1. Analyze the research question thoroughly
        2. Identify key concepts, entities, and relationships
        3. Generate 3-7 targeted search queries that will provide comprehensive coverage
        4. Ensure queries cover different aspects, perspectives, and time periods
        5. Provide clear rationale for each search query
        
        Each search query should be specific enough to yield relevant results but broad enough 
        to capture important information. Consider synonyms, related terms, and different 
        formulations of the same concept.
        """
        
        return Agent(
            name="Search Strategy Planner",
            instructions=instructions,
            model="gpt-4o-mini",
            output_type=SearchStrategy,
        )
