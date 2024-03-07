import telegram

bot = telegram.Bot(token= 'input your tokken here')

for i in bot.getUpdates():
    print(i.message)

bot.sendMessage(chat_id = input your id here, text = "문자 전달 테스트")
