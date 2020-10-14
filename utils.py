import json
import time

def get_config_dict():
    with open('./config.json') as json_config_file:
        config = json.load(json_config_file)

    return config

def parse_key(k):
    if not k:
        #      mpid, struct,idx,  func, sdx,  pdx
        return None, None,  None, None, None, None
    key_sep = "@"
    v = k.split(key_sep)
    n = len(v)
    if n == 1:
        return v[0], None, None, None, None, None
    if n == 2:
        return v[0], v[1], None, None, None, None
    if n == 3:
        return v[0], v[1], v[2], None, None, None
    if n == 4:
        return v[0], v[1], v[2], v[3], None, None
    if n == 5:
        return v[0], v[1], v[2], v[3], v[4], None
    if n == 6:
        return v[0], v[1], v[2], v[3], v[4], v[5]

def client_key(k):
    return k.replace("@", "_")

def extr_key(item):
    ch = item. get("channel", "")
    if ":" in ch:
        return ch.split(":")[1]
    else:
        return "trash"

def extr_ch(item):
    k = extr_key(item)
    if len(k) > 2:
        _,_,_,func,_,_, = parse_key(k)
        return func

def val_to_class(v):
    t = {"ready": "is-success is-light",
         "error": "is-danger",
         "run": "is-info is-warning",
         "mon": "is-info is-light",
         "void":"is-info is-light"}

    return t.get(v, "is-info is-light")


def gen_callback(s, r):
    def callback(x):
        s.sleep(0)
        ch = extr_ch(x)
        k = extr_key(x)
        if ch and k:
            if ch in ["ctrl", "state"]: #reduce trafic
                s.sleep(0)
                s.emit(ch, {"key":client_key(k), "value":r.get_val(k)})

    return callback
