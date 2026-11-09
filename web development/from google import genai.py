from google import genai
api_key = input("Paste your Gemini API Key here: ").strip()
client = genai.Client(api_key=api_key)

print("Learning Path Generator Agent") 

while True: 
    topic = input("\nEnter a topic to learn (or exit): ").strip() 
    if topic.lower() == "exit":
        print("Goodbye!")
        break
    if not topic:
        print("Please enter a topic.")  
        continue

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash", 
            contents=f"""Create a beginner-friendly learning path for: {topic}
Include prerequisites, 5 learning steps, practical projects, free learning resources to search for, and a weekly study plan.""",
        )
        print("\nYour Learning Path:\n", response.text or "No response received.")
    except Exception as e:
        err = str(e)
        if "429" in err or "RESOURCE_EXHAUSTED" in err:
            print("Gemini quota exceeded. Check your API usage and limits.")
        elif "API_KEY_INVALID" in err or "API key not valid" in err:
            print("Invalid API key. Check your Gemini API key.") 
        elif "404" in err or "NOT_FOUND" in err:
            print("Model not found. Verify the model name.")
        else:
            print("Error:", e)