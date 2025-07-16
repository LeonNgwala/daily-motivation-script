# daily_motivation.py
import random
from datetime import date

quotes = [
    "Keep pushing, success is around the corner.",
    "Discipline outlasts motivation.",
    "Code today, lead tomorrow.",
    "You only lose when you quit.",
    "Consistency beats intensity.",
    "Progress, not perfection.",
    "Your future self will thank you."
]

def get_quote():
    return random.choice(quotes)

if __name__ == "__main__":
    print(f"🗓️ {date.today()} Motivation:")
    print("💡", get_quote())
