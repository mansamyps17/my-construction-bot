import logging
import os
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# កំណត់ការបង្ហាញទិន្នន័យ Error (Log)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# API Token របស់អ្នក
TOKEN = '8905529352:AAELX8L7ouhPFxnFRSlaAdq6J_NzFe0EozE'

# 🌐 បង្កើត Web Server តូចមួយដើម្បីកុំឱ្យ Cloud Hosting (Render) បិទ Bot របស់យើងចោល
def run_dummy_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    print(f"Web Server កំពុងដើរលើ Port {port}")
    server.serve_forever()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        ['🏗️ មើលគម្រោងសំណង់', '💰 ប៉ាន់ស្មានតម្លៃសាងសង់'],
        ['📞 ទាក់ទងក្រុមហ៊ុន', '📍 ទីតាំងការិយាល័យ']
        ['📞 ផ្សេងៗ', '📍 កំណត់សម្គាល់']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    welcome_text = (
        "សួស្តីបាទ សាមី! ស្វាគមន៍មកកាន់ក្រុមហ៊ុនសំណង់របស់យើង។ 🙏\n"
        "តើខ្ញុំអាចជួយអ្វីអ្នកបានខ្លះនៅថ្ងៃនេះ? សូមជ្រើសរើស Menu ខាងក្រោម៖"
    )
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    if text == '🏗️ មើលគម្រោងសំណង់':
        await update.message.reply_text(
            "🚧 **គម្រោងបច្ចុប្បន្នរបស់យើង៖**\n\n"
            "1. វីឡាទោល ម៉ូដ Modern (ភ្នំពេញថ្មី) - បញ្ចប់បាន ៩០%\n"
            "2. ផ្ទះល្វែង E0, E1 (ផ្លូវជាតិលេខ ៦) - កំពុងបុកគ្រឹះ\n\n"
            "👉 លោកអ្នកអាចទាក់ទងមកកាន់លេខ 016-28-29-20 សម្រាប់ព័ត៌មានលម្អិត។"
        )
    elif text == '💰 ប៉ាន់ស្មានតម្លៃសាងសង់':
        await update.message.reply_text(
            "📊 **ការប៉ាន់ស្មានតម្លៃបឋម (តម្លៃមធ្យម)៖**\n\n"
            "• ផ្ទះល្វែង/ល្វែងទំនើប៖ $280 - $350 ក្នុងមួយម៉ែត្រការ៉េ\n"
            "• វីឡាកូនកាត់/វីឡាទោល៖ $380 - $550 ក្នុងមួយម៉ែត្រការ៉េ\n\n"
            "*(បញ្ជាក់៖ តម្លៃជាក់ស្តែងអាស្រ័យលើប្លង់ គ្រឹះដី និងគ្រឿងបង្គុំស្ថាបត្យកម្ម)*"
        )
    elif text == '📞 ទាក់ទងក្រុមហ៊ុន':
        await update.message.reply_text(
            "📞 **ព័ត៌មានទំនាក់ទំនង៖**\n\n"
            "• លេខទូរស័ព្ទ៖ 016 28 29 20 / 097 777 94 99\n"
            "• អ៊ីមែល៖ info@constructionco.com\n"
            "• ម៉ោងធ្វើការ៖ ចន្ទ - សៅរ៍ (7:30 AM - 5:00 PM)"
        )
    elif text == '📍 ទីតាំងការិយាល័យ':
        await update.message.reply_text(
            "📍 **ទីតាំងការិយាល័យកណ្តាល៖**\n\n"
            "មហាវិថីសហព័ន្ធរុស្ស៊ី, សង្កាត់ទឹកថ្លា, ខណ្ឌសែនសុខ, រាជធានីភ្នំពេញ។\n"
            "🔗 Link ផែនទី Google Maps: http://maps.google.com"
        )
    elif text == '📞 ផ្សេងៗ':
        await update.message.reply_text(
            "📍 **ផ្សេងៗ៖**\n\n"
            "មហាវិថីសហព័ន្ធរុស្ស៊ី, សង្កាត់ទឹកថ្លា, ខណ្ឌសែនសុខ, រាជធានីភ្នំពេញ។\n"
            "🔗 Link ផែនទី Google Maps: http://maps.google.com"
        )
    elif text == '📍 កំណត់សម្គាល់':
        await update.message.reply_text(
            "📍 **កំណត់សម្គាល់៖**\n\n"
            "មហាវិថីសហព័ន្ធរុស្ស៊ី, សង្កាត់ទឹកថ្លា, ខណ្ឌសែនសុខ, រាជធានីភ្នំពេញ។\n"
            "🔗 Link ផែនទី Google Maps: http://maps.google.com"
        )
    else:
        await update.message.reply_text("សូមជ្រើសរើស Menu ខាងក្រោម ដើម្បីឱ្យខ្ញុំងាយស្រួលជួយលោកអ្នក។")

def main() -> None:
    # ដើរតួជាអ្នកបើក Web Server ឱ្យដំណើរការដាច់ដោយឡែក
    threading.Thread(target=run_dummy_server, daemon=True).start()

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🚀 Bot កំពុងដំណើរការ...")
    application.run_polling()

if __name__ == '__main__':
    main()