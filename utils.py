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
