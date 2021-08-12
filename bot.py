from pyyoutube import Data
from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
import os 
BOT_TOKEN = os.environ.get("TOKEN","")
updater = Updater(BOT_TOKEN,use_context = True )

def start(updater,context):
 updater.message.reply_text('Hello Iam YouTube Thumbnail Downloader Bot  ')
 
def echo(updater,context):
 link = updater.message.text
 s = updater.message.reply_text('🧑‍💻🧑‍💻🧑‍💻')
 yt = Data("https://youtu.be/HhHzCfrqsoE")
 thumb = yt.thumbnails
 
 context.bot.send_photo(updater.message.chat.id,thumb,reply_to_message_id =updater.message.message_id)
 s.delete()
  
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.regex(r'^https?:\/\/?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/).{11}'),echo))

updater.start_polling()
updater.idle()
