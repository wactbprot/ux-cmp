import json



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

    return item.get("channel", ":").split(":")[1]

def extr_ch(item):
    # 'channel': '__keyspace@0__:ref@container@0@state@0@0'    
    k = extr_key(item)
    
    if len(k) < 2:
        return "trash"
    else:
        _,_,_,func,_,_, = parse_key(k)
        return func
