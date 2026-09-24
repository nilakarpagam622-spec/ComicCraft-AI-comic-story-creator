import google.generativeai as genai
API_KEY = "AQ.Ab8RN6IZAaXWmWRGshDdJJbwQ6CLvG_-CCWvN-JNPUkpC9HNlw"

genai.configure(api_key=API_KEY)

def generate_comic_story(prompt_text):
    model = genai.GenerativeModel('gemini-3.6-flash')
    
    prompt = f"Create a 4-panel comic strip script based on: '{prompt_text}'. Include Panel descriptions, character actions, and dialogues."
    
    print("\nGenerating comic script...\n")
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("==================================================")
    print("   ComicCraft: AI Comic Story Creator            ")
    print("==================================================\n")
    
    topic = input("Enter your comic story idea: ")
    
    try:
        result = generate_comic_story(topic)
        print("==================================================")
        print("           COMIC SCRIPT OUTPUT                    ")
        print("==================================================\n")
        print(result)
        print("\n==================================================")
    except Exception as e:
        print("\nError occurred:", e)
        print("Check your API Key! It must start with 'AIzaSy...'")
