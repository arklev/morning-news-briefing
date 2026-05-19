import google.generativeai as genai
import logging
from config import GEMINI_API_KEY

def summarize_news(articles):
    if not articles:
        return "לא נמצאו חדשות משמעותיות ב-12 השעות האחרונות."

    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-3.1-flash-lite')
        
        content = "\n".join([f"T: {a['title']}\nS: {a['summary']}\nL: {a['link']}" for a in articles])
        
        prompt = (
            "Summarize the following articles into the 5 most interesting news items. "
            "The output MUST be in Hebrew. "
            "For each item: "
            "1. Use a bullet point (•) instead of numbers to ensure correct alignment for Hebrew. "
            "2. Provide a concise summary. "
            "3. Include the link at the end of the item as [קרא עוד](URL). "
            "The output must be formatted clearly for a Discord webhook using markdown. "
            "DO NOT include any introductory or concluding text. "
            "Ensure the text flows naturally from right to left.\n\n"
            f"{content}"
        )
        
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        logging.error(f'AI Summarization failed: {e}')
        return "שגיאה ביצירת הסיכום. אנא בדוק את הלוגים."
