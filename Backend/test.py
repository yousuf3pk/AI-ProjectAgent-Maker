from modules.ai_agent.supervisor import build_supervisor

print("\n--- TEST 3: SUPERVISOR ---")

app = build_supervisor("groq")

response = app.invoke({
    "messages": [
        {"role": "user", "content": "What offers are available today?"}
    ]
})

print("\nSUPERVISOR RESPONSE:")
print(response["messages"][-1].content)