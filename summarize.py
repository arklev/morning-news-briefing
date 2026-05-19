import google.generativeai as genai
import logging
import json
import re
from config import GEMINI_API_KEY

def summarize_news(articles):
    if not articles:
        return []

    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-3.1-flash-lite')
        
        input_list = []
        for i, a in enumerate(articles):
            input_list.append('INDEX: ' + str(i) + '\nTITLE: ' + articles[i]['title'] + '\nSUMMARY: ' + articles[i]['summary'])
            
        content_str = '\n---\n'.join(input_list)
        
        prompt = (
            'Select the 5 most interesting news items from the list below. '
            'For each item, write a one-sentence summary in Hebrew. '
            'You MUST return the result in this exact JSON format: '
            '[ {"index": 0, "he_summary": "..."}, ... ] '
            'Return ONLY the JSON array. No other text.\n\n'
            + content_str
        )
        
        response = model.generate_content(prompt)
        text = response.text.strip()
        
        # Clean up JSON response without using backticks in the source code
        text = text.replace('json', '')
        for c in ['\x60']: # Hex for backtick
            text = text.replace(c, '')
        text = text.strip()
        
        selected_data = json.loads(text)
        
        results = []
        for item in selected_data:
            idx = int(item['index'])
            if 0 <= idx < len(articles):
                orig = articles[idx]
                results.append({
                    'title': orig['title'],
                    'summary': item['he_summary'],
                    'link': orig['link'],
                    'image': orig['image']
                })
        
        return results[:5]
    except Exception as e:
        logging.error('AI Summarization failed: ' + str(e))
        return []
