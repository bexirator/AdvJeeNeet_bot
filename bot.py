import telebot
import random
import json
import os
from myutils.question_picker import get_questions
from myutils.answer_checker import check_answer
from myutils.tips import get_tip

# 🔐 BOT TOKEN directly used here
BOT_TOKEN = "8059586677:AAFb4GIzD-OrrmO_mb90OeHVlZ87ACFdCLg"
bot = telebot.TeleBot(BOT_TOKEN)

special_usernames = ["@xemibleu", "@iiyyobiizz"]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.from_user.username and f"@{message.from_user.username}" in special_usernames:
        bot.reply_to(message, "🌸 You’re not just a user — you’re one half of a bond built over studies, chaos, and late-night doubts 💬📚❤️.")
    else:
        bot.reply_to(message, "👋 Welcome! Send /help to see all commands.")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "📚 *Exam Prep Bot Commands*\n\n"
        "🔹 `/jeemains 5` – Get 5 JEE Mains level questions (random)\n"
        "🔹 `/jeeadv 3` – Get 3 JEE Advanced level questions\n"
        "🔹 `/neet 4` – Get 4 NEET level questions\n\n"
        "🧠 Type your answer – bot will try to check it.\n"
        "🔍 Type `explain ache se` for a deep explanation.\n"
        "🈶 `/solve [question] in Hindi/Hinglish` – for language-specific solutions.\n"
        "📄 `/pdfjeemains2019 shift1` – Get official paper PDFs\n"
        "🎯 `/mocktest` – Full random test\n"
        "🧪 `/topic electrostatics 3`, `/difficulty easy 4` – topic/difficulty filters\n"
        "💡 `/tips` – Memory + exam tips\n"
    )
    bot.reply_to(message, help_text, parse_mode="Markdown")

@bot.message_handler(commands=['tips'])
def send_tips(message):
    bot.reply_to(message, get_tip())

@bot.message_handler(commands=['mocktest'])
def mock_test(message):
    questions = get_questions("jeemains", 10)
    for q in questions:
        bot.send_message(message.chat.id, q)

@bot.message_handler(func=lambda m: m.text.lower().startswith("/pdf"))
def send_pdf(message):
    parts = message.text[1:].split()
    exam_year = parts[0].replace("pdf", "")
    shift = parts[1] if len(parts) > 1 else ""
    filename = f"{exam_year}_{shift}.pdf" if shift else f"{exam_year}.pdf"
    filepath = os.path.join("pdfs", filename.lower())

    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            bot.send_document(message.chat.id, f)
    else:
        bot.reply_to(message, "❌ PDF not found.")

@bot.message_handler(commands=['jeemains', 'jeeadv', 'neet'])
def send_questions(message):
    parts = message.text.split()
    exam = message.text.split()[0][1:]
    count = int(parts[1]) if len(parts) > 1 else 5
    questions = get_questions(exam, count)
    for q in questions:
        bot.send_message(message.chat.id, q)

@bot.message_handler(func=lambda m: True)
def handle_answer(message):
    text = message.text.lower()
    if "explain ache se" in text:
        bot.reply_to(message, "📝 Here's a more detailed explanation...\n(This part is AI-generated)")
    elif "in hindi" in text or "in hinglish" in text:
        lang = "Hindi" if "hindi" in text else "Hinglish"
        bot.reply_to(message, f"🗣 Solution in {lang}:\n(This part is AI-generated)")
    elif "is this correct" in text or "sahi hai kya" in text:
        response = check_answer(message.text)
        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "✅ Answer received. Use `explain ache se` or ask in a specific language.")

bot.infinity_polling()