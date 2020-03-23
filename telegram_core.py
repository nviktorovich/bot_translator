import telebot
from sub.constant import Constant
from sub.options import UserOptions
import API_tester

bot = telebot.TeleBot(Constant.TELEGRAM_API_KEY)


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def translate_query(query):
	proposal = []
	try:
		for option in range(len(UserOptions.options['id'])):
			proposal.append(telebot.types.InlineQueryResultArticle(
				id=UserOptions.options['id'][option],
				title=UserOptions.options['title'][option],
				description=UserOptions.options['description'][option],
				thumb_url=UserOptions.options['thumb_url'][option], thumb_width=48, thumb_height=48,
				input_message_content=telebot.types.InputTextMessageContent(
					message_text=f'send by {query.from_user.first_name} (@{query.from_user.username})\n' +
					             API_tester.get_translate(UserOptions.options['message_text'][option][0],
					                                      UserOptions.options['message_text'][option][1], query.query)))
			)

		bot.answer_inline_query(query.id, proposal, cache_time=10)
	except Exception:
		print(Exception)


while True:
	bot.polling(none_stop=True, interval=0, timeout=0)
