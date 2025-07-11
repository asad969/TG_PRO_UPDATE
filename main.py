import os
from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")
bot = Bot(token=bot_token)

def send_update():
    now = datetime.now(ZoneInfo("Asia/Dhaka")).strftime("%d-%b-%y %I:%M %p")
    message = f"🕒 6H Live Signal Update ({now})\n\n" \
              "📊 BTCUSDT\nTrend: Uptrend\nStochRSI: 85 → 🔻 Sell Zone\n" \
              "RSI: 81 → Overbought\nMACD: Selling Pressure\nATR: Medium\n→ Entry: 59000\n→ TP: 60500\n→ SL: 58000"
    bot.send_message(chat_id=chat_id, text=message)

scheduler = BlockingScheduler(timezone="Asia/Dhaka")
scheduler.add_job(send_update, 'interval', hours=6)
scheduler.start()