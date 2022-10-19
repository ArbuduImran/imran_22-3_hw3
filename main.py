from aiogram.utils import executor
from config import dp
import logging
from handlers import client, callback, extra, admin, fsm_mentor

client.register_handlers_client(dp)
admin.register_handlers_ADMIN(dp)
callback.callback_query_handler(dp)
fsm_mentor.register_handlers_fsm(dp)
extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
