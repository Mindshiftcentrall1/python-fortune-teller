import time
import random
import os
from colorama import init, Fore, Style

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.05, color=Fore.WHITE):
    for char in text:
        print(f"{color}{char}", end='', flush=True)
        time.sleep(delay)
    print()

def display_ascii():
    art_options = [
        f"""{Fore.CYAN}
           .     .
        ...  :``..':
         : ````.'   :''::'
       ..:..  :     .'' :
   `.  :     `:.    .'     :
     :    :   :        :   :    :
      :   :   :         :  :   :
      :    :   :        : :    :
       :    :   :..''''``:::..'
        `....:::....'      ''
           CRYSTAL  BALL 🔮""",

        f"""{Fore.MAGENTA}
           .-''''-.
         .'        `.
        / _   __   _ \\
       : (_) (_'_) (_) :
       ;               ;
        \\             /
         `.         .'
           `-.___.-'
           PALM OF FATE ✋""",

        f"""{Fore.YELLOW}
           ✨✨✨✨✨✨✨
        ✨     STARS     ✨
         ✨   ABOVE YOU   ✨
           ✨✨✨✨✨✨✨"""
    ]
    print(random.choice(art_options))
    time.sleep(2)

def main():
    clear_screen()
    display_ascii()

    slow_print("\nYou have entered the mystic realm...\n", delay=0.07, color=Fore.LIGHTBLUE_EX)
    time.sleep(1)

    # Multiple themed questions
    questions = [
        "Will I become a successful coder?",
        "Is love in my near future?",
        "Should I take that job offer?",
        "Will I find happiness this year?",
        "Is wealth coming my way?",
        "Will my next project go viral?",
        "Is travel in the stars for me?",
        "Should I start my business idea?",
        "Will I meet someone special soon?",
        "Is now a good time to take risks?",
        "Will I overcome my challenges?",
        "Is peace coming into my life?",
        "Will I get that promotion?",
        "Is the universe guiding me?",
        "Is something unexpected coming?",
        "Should I invest in myself right now?",
        "Will I reconnect with someone from my past?",
        "Is this the right time to change direction?",
        "Will creativity guide my next steps?",
        "Am I ready for the next big thing?"
    ]

    responses = [
        "✨ Absolutely yes – the stars are aligned.",
        "🌙 Unclear right now, ask again later.",
        "🔮 All signs point to yes.",
        "☁️ It is cloudy – focus and try again.",
        "🔥 Definitely – but with hard work.",
        "❄️ Not likely... but surprises await.",
        "🧿 Yes – a new opportunity is coming.",
        "🌌 The universe says 'maybe'.",
        "💫 It is written in the stars.",
        "🌠 Only if you trust your path.",
        "🌞 A bright outcome is within reach.",
        "🌿 Patience will reveal the answer.",
        "🌀 The future shifts — keep watching.",
        "🦋 Change is near — embrace it.",
        "🌊 A wave of luck is on its way.",
        "🪐 Your instincts are correct — follow them.",
        "🧘 Calm your mind — the answer will appear.",
        "💎 You are more ready than you think.",
        "🎭 Look beyond the surface.",
        "🛤️ A new path is opening soon.",
        "🕰️ Time is on your side.",
        "🎯 Focus brings the future into view.",
        "📚 Learn first, then leap.",
        "🧭 Your inner compass knows the way.",
        "🌳 Growth will come from stillness.",
        "🌈 Positivity will attract results.",
        "🛡️ Protect your energy, then decide.",
        "🚀 A bold move will change everything.",
        "🕊️ Forgiveness brings fortune.",
        "✨ A moment of clarity is coming."
    ]

    for i in range(15):
        clear_screen()
        display_ascii()

        slow_print(f"\n🧘 Fortune #{i + 1}/15\n", delay=0.07, color=Fore.LIGHTBLUE_EX)
        time.sleep(1)

        question = random.choice(questions)
        slow_print(f"Your question: {question}\n", delay=0.06, color=Fore.LIGHTGREEN_EX)
        time.sleep(1.5)

        slow_print("Let me gaze into the crystal ball... 🔮\n", delay=0.08, color=Fore.LIGHTMAGENTA_EX)
        time.sleep(2)

        answer = random.choice(responses)
        slow_print("The spirits whisper...", delay=0.06, color=Fore.LIGHTYELLOW_EX)
        time.sleep(1)

        slow_print(f"\n{answer}\n", delay=0.08, color=Fore.LIGHTCYAN_EX)
        time.sleep(5)

        slow_print("🌙 The vision fades...\n", delay=0.06, color=Fore.LIGHTBLUE_EX)
        time.sleep(3)

    slow_print("\n🌌 Thank you for visiting the Fortune Teller. Until next time...\n", delay=0.07,
               color=Fore.LIGHTMAGENTA_EX)
    time.sleep(3)


if __name__ == "__main__":
    main()