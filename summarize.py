import google.generativeai as genai
import logging
from config import GEMINI_API_KEY

def summarize_news(articles):
    if not articles:
        return "לא נמצאו חדשות משמעותיות ב-12 השעות האחרונות."

    try:
        genai.configure(api_key=GEMINI_API_KEY)
        # Using gemini-3.1-flash-lite for maximum token efficiency as requested
        model = genai.GenerativeModel('gemini-3.1-flash-lite')
        
        content = "\n".join([f"T: {a['title']}\nS: {a['summary']}\nL: {a['link']}" for a in articles])
        
        prompt = (
            "Summarize the following articles into the 5 most interesting news items. "
            "For each item, provide a concise summary and include the original link. "
            "The output MUST be in Hebrew and formatted clearly for a Discord webhook using markdown. "
            "DO NOT include any introductory or concluding text like 'Here is the summary' or 'הנה סיכום'. "
            "Just provide the news items themselves.\n\n"
            f"{content}"
        )
        
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        logging.error(f'AI Summarization failed: {e}')
        return "שגיאה ביצירת הסיכום. אנא בדוק את הלוגים."
