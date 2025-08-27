"""
Research Orchestrator - Coordinates the entire research workflow
"""

import asyncio
from typing import AsyncGenerator
from agents import Runner, trace, gen_trace_id

from ..agents.search_planner import SearchPlanner, SearchStrategy
from ..agents.web_researcher import WebResearcher
from ..agents.report_writer import ReportWriter, ResearchReport
from ..agents.notification_sender import ReportFormatter


class ResearchOrchestrator:
    """
    Main orchestrator that coordinates the research workflow across multiple agents.
    Manages the entire process from query planning to final report display.
    """

    def __init__(self):
        self.search_planner = SearchPlanner()
        self.web_researcher = WebResearcher()
        self.report_writer = ReportWriter()
        self.report_formatter = ReportFormatter()

    async def execute_research(self, query: str) -> AsyncGenerator[str, None]:
        """
        Execute the complete research process for a given query.
        
        Args:
            query: The research question to investigate
            
        Yields:
            Status updates throughout the process
        """
        trace_id = gen_trace_id()
        
        with trace("Research Execution Trace", trace_id=trace_id):
            # Log trace URL
            trace_url = f"https://platform.openai.com/traces/trace?trace_id={trace_id}"
            yield f"🔍 Research Trace: {trace_url}"
            
            # Phase 1: Plan research strategy
            yield "📋 Planning research strategy..."
            search_strategy = await self._create_search_strategy(query)
            yield f"✅ Strategy planned: {len(search_strategy.search_queries)} search queries identified"
            
            # Phase 2: Execute web searches
            yield "🌐 Executing web searches..."
            search_results = await self._conduct_web_research(search_strategy)
            yield f"✅ Research complete: {len(search_results)} sources analyzed"
            
            # Phase 3: Generate comprehensive report
            yield "📝 Generating comprehensive report..."
            research_report = await self._generate_research_report(query, search_results)
            yield "✅ Report generated successfully"
            
            # Phase 4: Format report for display
            yield "📄 Formatting report for display..."
            formatted_report = self.report_formatter.format_report_for_display(research_report.markdown_content)
            yield "✅ Report formatted and ready for display"
            
            # Return final report
            yield "🎉 Research process completed!"
            yield formatted_report

    async def _create_search_strategy(self, query: str) -> SearchStrategy:
        """Create an optimized search strategy for the research query."""
        print(f"Creating search strategy for: {query}")
        
        result = await Runner.run(
            self.search_planner.agent,
            f"Research Query: {query}"
        )
        
        strategy = result.final_output_as(SearchStrategy)
        print(f"Planned {len(strategy.search_queries)} search queries")
        return strategy

    async def _conduct_web_research(self, strategy: SearchStrategy) -> list[str]:
        """Execute all planned web searches and collect results."""
        print("Starting web research...")
        
        # Create concurrent search tasks
        search_tasks = [
            asyncio.create_task(self._execute_single_search(search_item))
            for search_item in strategy.search_queries
        ]
        
        results = []
        completed_count = 0
        
        # Process results as they complete
        for task in asyncio.as_completed(search_tasks):
            result = await task
            if result:
                results.append(result)
            completed_count += 1
            print(f"Research progress: {completed_count}/{len(search_tasks)} queries completed")
        
        print(f"Web research completed with {len(results)} successful results")
        return results

    async def _execute_single_search(self, search_item) -> str | None:
        """Execute a single web search query."""
        search_input = f"Search Query: {search_item.query}\nSearch Rationale: {search_item.rationale}"
        
        try:
            result = await Runner.run(
                self.web_researcher.agent,
                search_input
            )
            return str(result.final_output)
        except Exception as e:
            print(f"Search failed for '{search_item.query}': {e}")
            return None

    async def _generate_research_report(self, query: str, search_results: list[str]) -> ResearchReport:
        """Generate a comprehensive research report from collected data."""
        print("Generating research report...")
        
        report_input = f"Original Research Query: {query}\nCollected Research Data: {search_results}"
        
        result = await Runner.run(
            self.report_writer.agent,
            report_input
        )
        
        report = result.final_output_as(ResearchReport)
        print("Research report generated successfully")
        return report
