from application.im_bot.telegram_message_handler import TelegramMessageHandler

"""
Started Service Bot
"""
telegram = TelegramMessageHandler()
telegram.run_bot()