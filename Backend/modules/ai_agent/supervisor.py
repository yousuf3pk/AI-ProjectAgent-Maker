
"""Supervisor: routes customer requests to specialized agents."""

from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor
from modules.ai_agent.graph import create_chat_model
from modules.ai_agent.tools import (
    fetch_menu,
    validate_order_id,
    log_complaint,
    get_offer,
)


def build_supervisor(llm="groq"):
    model = create_chat_model(llm)

    # Menu specialist
    menu_agent = create_react_agent(
        model=model,
        tools=[fetch_menu],
        name="menu_agent",
        prompt=(
            "You handle menu and price inquiries. "
            "Always use fetch_menu to retrieve menu information. "
            "Prices are in PKR. Use Rs., never the peso sign."
        ),
    )

    # Complaint specialist
    complaint_agent = create_react_agent(
        model=model,
        tools=[validate_order_id, log_complaint],
        name="complaint_agent",
        prompt=(
            "You handle customer complaints. Collect customer name, "
            "phone, order ID and complaint. Check the order ID with "
            "validate_order_id, then save with log_complaint only "
            "if valid. Ask for missing details. "
            "Never invent a complaint ID."
        ),
    )

    # Offer specialist
    offer_agent = create_react_agent(
        model=model,
        tools=[get_offer],
        name="offer_agent",
        prompt=(
            "You handle customer offer inquiries. "
            "Always call get_offer to retrieve available offers. "
            "Return only one matching offer as a plain string. "
            "Never invent or modify offer details. "
            
        ),
    )

    # Supervisor
    supervisor = create_supervisor(
        agents=[
            menu_agent,
            complaint_agent,
            offer_agent
        ],
        model=model,
        prompt=(
            "You manage customer support for Xander Restaurant. "
            "Route menu and price questions to menu_agent. "
            "Route complaints to complaint_agent. "
            "Route promotional offer questions to offer_agent. "
            "Handle greetings yourself briefly. "
            "Return the worker's answer without adding unrelated information."
        ),
    )

    return supervisor.compile()
