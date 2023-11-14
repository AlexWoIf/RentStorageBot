from environs import Env


env = Env()
env.read_env()

LOG_LEVEL = env.str('LOG_LEVEL', 'INFO')

BOT_TOKEN = env.str('BOT_TOKEN')
TG_API = env.str('TG_API', "https://api.telegram.org/bot")
