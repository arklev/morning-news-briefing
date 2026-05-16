import google.generativeai as genai
import logging
from config import GEMINI_API_KEY

def summarize_news(articles):
    if not articles:
        return "No significant news found in the last 12 hours."

    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-3-flash-preview')
        
        # Minimized input format
        content = "\n".join([f"T: {a['title']}\nS: {a['summary']}" for a in articles])
        
        prompt = (
            "Summarize the following into a VERY SHORT briefing (max 3-5 bullet points). "
            "Focus on critical Tech, Finance, and AI news only. "
            "Language: English. No fluff. Be extremely concise.\n\n"
            f"{content}"
        )
        
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        logging.error(f'AI Summarization failed: {e}')
        return "Error generating summary. Please check logs."
