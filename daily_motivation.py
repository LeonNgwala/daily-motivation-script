# daily_motivation.py
import random
import sys
from datetime import date

quotes = {
    "success": [
        ("Discipline outlasts motivation.", "Unknown"),
        ("You only lose when you quit.", "Napoleon Hill"),
        ("Keep pushing, success is around the corner.", "Eric Thomas"),
    ],
    "growth": [
        ("Progress, not perfection.", "Marie Forleo"),
        ("Fail forward and fail often.", "John C. Maxwell"),
        ("Your future self will thank you.", "Anonymous"),
    ],
    "code": [
        ("Code today, lead tomorrow.", "Lutho"),
        ("Talk is cheap. Show me the code.", "Linus Torvalds"),
        ("Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "Martin Fowler"),
    ]
}

def get_quote(category=None):
    if category is None or category not in quotes:
        all_quotes = sum(quotes.values(), [])
        return random.choice(all_quotes)
    return random.choice(quotes[category])

if __name__ == "__main__":
    category = sys.argv[1].lower() if len(sys.argv) > 1 else None

    if category and category not in quotes:
        print(f"⚠️ Unknown category '{category}'. Available categories: {', '.join(quotes.keys())}\n")

    quote, author = get_quote(category)
    print(f"🗓️ {date.today()} Motivation")
    print(f"💡 {quote}\n— {author}")
