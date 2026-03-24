import os
import sys
from openclaw import OpenClaw

def run_horror_pipeline():
    # Diagnostic: Tell us what version the cloud is running
    print(f"--- SYSTEM CHECK: Python {sys.version} ---")
    
    try:
        # Initialize the 2026 Engine
        client = OpenClaw(api_key=os.getenv("OPENAI_API_KEY"))

        print("--- PHASE 1: THE HOOK ---")
        hook = client.generate(
            prompt="Write one 20-word scary story hook about a haunted mirror.",
            model="gpt-4o"
        )
        print(f"Hook: {hook}")

        print("--- PHASE 2: THE SCRIPT ---")
        script = client.generate(
            prompt=f"Write a 200-word scary story based on this hook: {hook}",
            model="gpt-4o"
        )
        print("Script generated successfully.")
        
        print("--- PHASE 3: SUCCESS ---")

    except Exception as e:
        print(f"SYSTEM ERROR: {e}")

if __name__ == "__main__":
    run_horror_pipeline()
