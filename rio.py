import logging
import redis
import utils

logging.basicConfig(level=logging.DEBUG)

class Rio:
    def __init__(self):
        r = utils.get_config_dict().get('redis')
        self.host = r.get('host')
        self.port = r.get("port")
        self.db = r.get("db")
        self.init()
        logging.info('initialization complete')

    def init(self):
        logging.info('make server')
        self.srv = redis.StrictRedis(host=self.host, port=self.port, db=self.db, decode_responses=True)

    def get_pubsub(self):
        logging.info('make pubsub')
        self.pubsub = self.srv.pubsub()
