from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1896596326  # my telegram ID
    OWNER_USERNAME = "MuhYo07"  # my telegram username
    API_KEY = "5577188246:AAGKQlaGUklJ2wfaPu2uaUsdot-dsS0sDzE"  # my api key, as provided by the botfather
    MESSAGE_DUMP = '-1001890464774' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1896596326]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']