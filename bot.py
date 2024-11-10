# import everything
import telegram
import random
import logging
import os

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
    Updater,
)

List_Tota = ['He hates squid because of its texture',
             'He actually cannot handle cold very well',
             'He stays up late to read novels sometimes',
             'He loves the coffee made by MEIKO and requests for the same blend everytime because it is very comforting',
             "While his mother's cookies are slightly burnt, Toya still loves them",
             "He once fell asleep on his father's music books while reading them",
             "Toya went to Vienna as a child",
             "Toya has two brothers, of which none have their appearances known",
             'He once thought a barbeque fork was a tuning fork',
             'He caught a bear in a claw machine just because he thought the clothing was nicely made',
             'Toya can speak english',
             'The ginger cat that snuggles up to Toya is a street cat',
             'Toya knows how to make cotton candy',
             'He originally was supposed to go to a fancy prepatory school, but used Tsukasa as a leverage so he could join Akito',
             'He likes mystery novels',
             'He wants to go autumn leaf picking, but is not sure if anyone would join him',
             'He likes the sound of the wind chimes his mother puts up in the summer',
             'He planned a fancy party for MEIKO inspired by a party he went to when he was a child',
             'He has a tendency to mumble things to himself when he thinks',
             'He was so serious with his customer greeting he ended up scaring Rin and Len',
             'He gave his father a presentation to list out why he should go camping',
             'He learnt sewing from Mizuki',
             'During BURN MY SOUL, Akito noticed that Toya barely kept his eyes open, leading to him sleeping on the sofa backstage',
             'His camping trip with VBS was the first time Toya held a knife',
             'He likes to help Akito in studying, finding methods that work for Akito',
             "Tsukasa put on a show for Toya's birthday about a boy on a journey to make lots of friends, only for Toya to realise the boy was a depiction of himself",
             'He is exceptionally good at crane games and its physics',
             'A bird landed on his head while singing',
             'He is fascinated by the white smoke that comes out whenever we breathe in cold weather',
             'Toya got Akito running shoes as a birthday gift',
             'https://www\.youtube\.com/watch\?v\=bxi1UpAParc',
             'Did you know the master chart of utsuro wo aogu has a combo of 1112 \?',
             ]

Response = ['Are the birds pretty today\?',
             "I\'m a cube\, I\'m a cube\, I\'m a cube cube cube",
             "Mawaru sekai ni hibiku youna kokoro ga odoru melody",
             'Watch: https://www\.youtube\.com/watch\?v\=dQw4w9WgXcQ',
             'Do you want to know where Toyaland is\?',
             'Nagai yoru no hate ni\.\.\. Watch this today\! https://www\.youtube\.com/watch\?v\=bxi1UpAParc',
             'CHUNITHM TOYA PLUS',
             'Buy a Toya cube for your health today',
             "Do you think Akito has a cube version of himself too?",
             "Here\, have a cupcake\!",
             'Ongeki bright TOYA',
             'maimaiDX TOYA',
             ]

global bot
global TOKEN

itemlink = ""
detail = ""

TOKEN = "7191936518:AAFF3c_6vfTbYbxwIUV-Y__tUk5zgniOij4"
bot = telegram.Bot(token="7191936518:AAFF3c_6vfTbYbxwIUV-Y__tUk5zgniOij4")

linktype = "https://"

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.ERROR)

logger = logging.getLogger(__name__)

ACTION, TYPE, USERNAME, LINK, REQTYPE, NOTES, SUMMARY, RANDOM, RANDOMV2, CHAT = range(10)

async def post_init(application: Application) -> None:
    await application.bot.set_my_commands([('start', 'Starts the bot')])

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text('''\U0001F916*Welcome to Cube Bot*\U0001F916\n
                                    \nThis bot was made for use for Aoyagi Cube Club \(\@aoyagiclub\) mainly for split requests and GO requests\.   
                                    \n*Main commands*\n> \-/start: Starts me \n> \-/help: Sends this message
                                    \nPlease click *"Request GO/ Split"* for any channel requests\; The rest of the features are just for a bit of fun\. If any split requests are made through those they *WILL NOT* be made known to me
                                    \nIf there are any bugs\, please message \@toyalove\.
                                    \nBot maintenance is usually every week or before a major merch release\; If the bot is unusable before a merch drop it is usually the case\.
                                    \nI usually look at requests from this bot faster than DMs as the database is easier to access\; However, *if you have questions about your request\(s\) please DM me instead\.*
                                    \nFrom\: a 10cm little helper from toyaland \U0001F499
                                    \n||Fun fact\: This bot is beta tested by my friends so thank you \:\)||
                                    ''',
                parse_mode=ParseMode.MARKDOWN_V2
              )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = [["Request GO/ Split", "Talk", "Mystery"]]

    await update.message.reply_text(
        "Hi \! I am a Toya Cube\. "
        "What would you like to do today \U0001F47E\? \n", parse_mode= ParseMode.MARKDOWN_V2
        ,
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Anything you like"
        ),
    )

    print(update.message.text)

    return ACTION

async def talk(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    user = update.message.from_user
    logger.info("Request of %s: %s", user.first_name, update.message.text)
    print(update.message.text)
    await update.message.reply_text(
        '''Feel free to type anything \(do note I do not replace actual humans so I am unable to give advice\)\n\n*This feature should not be used for splits\/ GO requests*''', parse_mode= ParseMode.MARKDOWN_V2,
    )
    return RANDOM

async def talkv2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    user = update.message.from_user
    logger.info("Request of %s: %s", user.first_name, update.message.text)
    print(update.message.text)
    RANDOM2 = random.choice(Response)
    await update.message.reply_text(
        f'''{RANDOM2} \n\(Type to continue\)''', parse_mode= ParseMode.MARKDOWN_V2,
    )
    return RANDOMV2
    

async def thank(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = [["Yes", "No"]]
    user = update.message.from_user
    logger.info("Request of %s: %s", user.first_name, update.message.text)
    print(update.message.text)
    await update.message.reply_text(
        "Thank you for talking to me today :), Anything else?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Continue?"
        ),
    )
    return CHAT

async def mystery(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    user = update.message.from_user
    logger.info("Request of %s: %s", user.first_name, update.message.text)
    print(update.message.text)
    Random1 = random.choice(List_Tota)

    await update.message.reply_text(
        f'''Random Facts About Toya\:\n\n> \U0001F48C {Random1}\n\nThank you for tuning in to Toya facts\.''',
        parse_mode=ParseMode.MARKDOWN_V2,
    )
    return ConversationHandler.END

async def merchtype(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = [["Badge", "Epick", "Other Proseka merch", "Other series"]]

    await update.message.reply_text(
        "Please let me know the merch category\.\U0001F47E", parse_mode= ParseMode.MARKDOWN_V2
        ,
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Waiting for merch type..."
        ),
    )
    print(update.message.text)
    return TYPE

async def user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """asks for user"""
    user = update.message.from_user
    logger.info("Request of %s: %s", user.first_name, update.message.text)
    print(update.message.text)
    await update.message.reply_text(
        "Okay\! Before we continue\, please let me know your username \(ie\.\@toyalove\) \U00002615", parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=ReplyKeyboardRemove(),
    )

    return USERNAME

async def link(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """asks for link"""
    global requser
    requser = update.message.text
    print(requser)
    user = update.message.from_user
    logger.info("Request of %s: %s", user.first_name, update.message.text)
    print(update.message.text)
    await update.message.reply_text(
        "I see\! Please send me the link to the item/site\, "
        "so I know what you\'re looking for\.\U00002615 \n>Please feel free to /cancel if you change your mind\. \n>\U0000203C I only accept links\! Raw text is not accepted", parse_mode=ParseMode.MARKDOWN_V2,
    )

    return LINK

async def request(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    global itemlink
    itemlink = update.message.text
    reply_keyboard = [["Split", "GO"]]
    print(itemlink)
    logger.info("User %s sending notes", user.first_name)
    await update.message.reply_text(
        '''Please let me know what the request is for:''',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Waiting for request type..."
        ),
    )
    return REQTYPE

async def notes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    global typeofreq
    typeofreq = update.message.text
    print(itemlink)
    logger.info("User %s sending notes", user.first_name)
    await update.message.reply_text(
        '''\U0001F47E Do you have any additional requests\?\n> Not limited to ie\. Splits\, Price range\, Items to order\, Preorder deadline\, Instocks\?
        \n\- Please let me know who you are claiming if requesting for a split\n\- If splitting multiple boxes\, please state the *quantity* of boxes or I will assume one box
        \nMore details about your request will make it easier for me\!\n\nElse\, if there are no additional requests\, please send "nil"'''
        ,parse_mode=ParseMode.MARKDOWN_V2
    )

    return NOTES


async def bio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    global detail
    detail =  update.message.text
    print(detail)
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    print(detail)
    print(itemlink)
    await update.message.reply_text(
        f'''Request stored in the cube; Thank you! Here's the summary of your request:\n\nRequest From: {requser}\n>Item: {itemlink}\n>Type: {typeofreq} \n>Detail: {detail}'''
                                    )
    await send(f'''Request From: {requser}\nItem: {itemlink}\nType: {typeofreq} \nDetail: {detail}''',-1002204726204)
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! When you have something for me please come back!", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

async def send(msg, chat_id, token="7191936518:AAFF3c_6vfTbYbxwIUV-Y__tUk5zgniOij4"):
    bot = telegram.Bot(token=token)
    bot.initialize
    await bot.sendMessage(chat_id=chat_id, text=msg)

def main() -> None:
    application = Application.builder().token("7191936518:AAFF3c_6vfTbYbxwIUV-Y__tUk5zgniOij4").post_init(post_init).build()
  
    # Port is given by Heroku
    PORT = os.environ.get('PORT')
  
     # Set up the Updater
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN,
                          webhook_url=f"https://cubismbot-ce9e03348913.herokuapp.com/{TOKEN}")
    updater.idle()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            ACTION: [
                MessageHandler(filters.Regex("^(Request GO/ Split)$"), merchtype),
                MessageHandler(filters.Regex("^(Talk)$"), talk),
                MessageHandler(filters.Regex("^(Mystery)$"), mystery),
                ],
            TYPE:[
                MessageHandler(filters.Regex("^(Badge)$"), user),
                MessageHandler(filters.Regex("^(Epick)$"), user),
                MessageHandler(filters.Regex("^(Other Proseka merch)$"), user),
                MessageHandler(filters.Regex("^(Other series)$"), user),
                ],
            USERNAME: [MessageHandler(filters.TEXT, link)],
            LINK: [MessageHandler(filters.Entity('url'), request)],
            REQTYPE: [MessageHandler(filters.TEXT, notes)],
            NOTES: [MessageHandler(filters.TEXT & (~filters.COMMAND), bio)],
            RANDOM: [MessageHandler(filters.TEXT, thank)],
            CHAT: [
                MessageHandler(filters.Regex("^(Yes)$"), talkv2),
                MessageHandler(filters.Regex("^(No)$"), cancel),
                ],
            RANDOMV2: [MessageHandler(filters.TEXT, thank)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("help", help_command))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()

