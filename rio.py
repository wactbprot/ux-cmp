import logging
import redis
import utils
 
logging.basicConfig(level=logging.DEBUG)

class Rio:
    def __init__(self, config):
        r = config.get('redis')
        self.host = r.get('host')
        self.port = r.get("port")
        self.db = r.get("db")
        self.init()
        logging.info('initialization complete')

    def init(self):
        logging.info('make server')
        self.srv = redis.Redis(host=self.host, port=self.port, db=self.db, decode_responses=True)
        self.p = self.srv.pubsub()
        
    def subscribe(self, pat, callback): 
        logging.info('subscribe *')
        self.p.psubscribe(**{pat: callback})
        self.thread = self.p.run_in_thread(sleep_time=0.1)
        
    def get_keys(self, pat):
        return self.srv.keys(pat)

    def get_val(self, k):
        return self.srv.get(k)
