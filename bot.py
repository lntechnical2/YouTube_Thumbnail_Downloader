from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
import  pafy 
import os 
BOT_TOKEN = os.environ.get("TOKEN","")
updater = Updater(BOT_TOKEN,use_context = True )

def start(updater,context):
 updater.message.reply_text('Hello Iam YouTube Thumbnail Downloader Bot  ')
 
def echo(updater,context):
 link = updater.message.text
 video = pafy.new(link) 
 id  = video.videoid
 thumb = f"https://i.youtube.com/vi/{id}/sddefault.jpg"
 context.bot.send_photo(updater.message.chat.id,thumb,reply_to_message_id =updater.message.message_id)
  
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.regex(r'^https?:\/\/?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/).{11}'),echo))

updater.start_polling()
updater.idle()
