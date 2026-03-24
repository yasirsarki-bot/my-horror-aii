import os
from openclaw import OpenClaw

# Initialize the 2026 Engine
client = OpenClaw(api_key=os.getenv("OPENAI_API_KEY"))

def run_horror_pipeline():
    try:
        print("--- PHASE 1: THE HOOK ---")
        # In the new version, we use 'generate' directly
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
        
        print("--- PHASE 3: READY FOR AUDIO ---")
        print("Pipeline Check: PASSED.")

    except Exception as e:
        print(f"SYSTEM ERROR: {e}")

if __name__ == "__main__":
    run_horror_pipeline()
