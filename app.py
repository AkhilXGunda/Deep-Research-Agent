"""
Deep Research System - Gradio Deploy
"""

import os
from research_system.interface.web_interface import ResearchWebInterface

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Create and launch the interface
interface = ResearchWebInterface()
interface.interface.launch(
    server_name="0.0.0.0",
    server_port=7860,
    share=False,
    inbrowser=False,
    show_error=True,
    quiet=False
)
