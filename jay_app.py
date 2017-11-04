from application.server import server_prod, server_local
from application.im.telegram.telegram_message_handler import TelegramMessageHandler

#server_prod()
server_local()
#telegram = TelegramMessageHandler()
#telegram.run_bot()