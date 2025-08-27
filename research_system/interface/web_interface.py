"""
Web Interface - Gradio-based user interface for the research system
"""

import gradio as gr
from dotenv import load_dotenv

from ..core.research_orchestrator import ResearchOrchestrator


class ResearchWebInterface:
    """
    Web-based user interface for the research system.
    Provides an intuitive way to interact with the research capabilities.
    """

    def __init__(self):
        load_dotenv(override=True)
        self.orchestrator = ResearchOrchestrator()
        self.interface = self._create_interface()

    def _create_interface(self) -> gr.Blocks:
        """Create the Gradio web interface."""
        with gr.Blocks(
            title="Deep Research System",
            theme=gr.themes.Default(primary_hue="sky"),
            css="""
            .gradio-container {
                max-width: 1200px !important;
                margin: 0 auto !important;
            }
            """
        ) as interface:
            
            # Header
            gr.Markdown(
                """
                # 🔍 Deep Research System
                ### AI-Powered Comprehensive Research Platform
                
                Enter your research question below and get a detailed, comprehensive report 
                generated through intelligent web research and analysis.
                """
            )
            
            with gr.Row():
                with gr.Column(scale=3):
                    # Input section
                    gr.Markdown("### 📝 Research Query")
                    query_input = gr.Textbox(
                        label="What would you like to research?",
                        placeholder="e.g., What are the latest developments in quantum computing?",
                        lines=3,
                        max_lines=5
                    )
                    
                    # Control buttons
                    with gr.Row():
                        start_button = gr.Button(
                            "🚀 Start Research", 
                            variant="primary",
                            size="lg"
                        )
                        clear_button = gr.Button(
                            "🗑️ Clear", 
                            variant="secondary"
                        )
                
                with gr.Column(scale=1):
                    # Status indicator
                    gr.Markdown("### 📊 Research Status")
                    status_display = gr.Markdown(
                        "Ready to begin research...",
                        elem_classes=["status-box"]
                    )
            
            # Progress section
            with gr.Row():
                gr.Markdown("### 📈 Research Progress")
                progress_output = gr.Markdown(
                    "Research will begin when you click 'Start Research'",
                    elem_classes=["progress-box"]
                )
            
            # Results section
            with gr.Row():
                gr.Markdown("### 📄 Research Report")
                report_output = gr.Markdown(
                    "Your comprehensive research report will appear here...",
                    elem_classes=["report-box"]
                )
            
            # Event handlers
            start_button.click(
                fn=self._execute_research,
                inputs=[query_input],
                outputs=[status_display, progress_output, report_output]
            )
            
            query_input.submit(
                fn=self._execute_research,
                inputs=[query_input],
                outputs=[status_display, progress_output, report_output]
            )
            
            clear_button.click(
                fn=self._clear_interface,
                inputs=[],
                outputs=[query_input, status_display, progress_output, report_output]
            )
        
        return interface

    async def _execute_research(self, query: str) -> tuple[str, str, str]:
        """
        Execute the research process and return status updates.
        
        Args:
            query: The research question to investigate
            
        Returns:
            Tuple of (status, progress, report)
        """
        if not query.strip():
            return (
                "❌ Please enter a research query",
                "No research started",
                "Enter a query to begin research"
            )
        
        status_messages = []
        progress_messages = []
        final_report = ""
        
        try:
            async for update in self.orchestrator.execute_research(query):
                if "🔍 Research Trace:" in update:
                    status_messages.append(update)
                elif "✅" in update or "📋" in update or "🌐" in update or "📝" in update or "📄" in update:
                    progress_messages.append(update)
                else:
                    final_report = update
            
            # Combine messages
            status = "\n".join(status_messages) if status_messages else "✅ Research completed successfully"
            progress = "\n".join(progress_messages) if progress_messages else "Research process completed"
            
            return status, progress, final_report
            
        except Exception as e:
            error_msg = f"❌ Research failed: {str(e)}"
            return error_msg, "Research process encountered an error", ""

    def _clear_interface(self) -> tuple[str, str, str, str]:
        """Clear all interface elements."""
        return "", "Ready to begin research...", "", "Your comprehensive research report will appear here..."

    def launch(self, **kwargs):
        """Launch the web interface."""
        self.interface.launch(
            inbrowser=True,
            share=False,
            **kwargs
        )


def main():
    """Main entry point for the web interface."""
    interface = ResearchWebInterface()
    interface.launch()


if __name__ == "__main__":
    main()
