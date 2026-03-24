from openclaw import Agent, Task

# 1. DEFINE THE WORKERS
idea_agent = Agent(name="Idea_Gen", model="gpt-4-turbo")
script_agent = Agent(name="Script_Writer", model="gpt-4-turbo")
voice_agent = Agent(name="Voice_Master", model="gpt-4-turbo")

def run_horror_pipeline():
    # --- STEP 1: GENERATE THE HOOK ---
    print("Step 1: Generating Hook...")
    hook_task = Task(
        description="Create a 1-sentence viral horror story hook about urban legends.",
        agent=idea_agent
    )
    story_hook = hook_task.execute() 
    print(f"Hook Created: {story_hook}")

    # --- STEP 2: WRITE THE SCRIPT ---
    print("Step 2: Writing Script...")
    script_task = Task(
        description=f"Write a 500-word scary story based on this hook: {story_hook}. Focus on psychological dread.",
        agent=script_agent
    )
    full_script = script_task.execute()
    print("Script finished.")

    # --- STEP 3: CONVERT TO AUDIO (The ElevenLabs Connection) ---
    print("Step 3: Generating Audio...")
    # This calls your ElevenLabs API automatically
    voice_task = Task(
        description=f"Convert this story into audio using a deep, gravelly male voice: {full_script}",
        agent=voice_agent,
        tool="elevenlabs_tts" # This is the 'skill' we installed
    )
    audio_file_path = voice_task.execute()
    
    print(f"SUCCESS! Your horror story is ready at: {audio_file_path}")

if __name__ == "__main__":
    run_horror_pipeline()
