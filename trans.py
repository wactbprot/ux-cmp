from flask import render_template
import utils

def state_html(rio, mp_id, struct, idx):
    state_keys = rio.get_keys("{}@{}@{}@state@*".format( mp_id, struct, idx))
    if not state_keys:
        return "404"

    state = {}
    for state_key in state_keys:
        _, _, _, _, j, k = utils.parse_key(state_key)
        if not state.get(j):
            state[j] = {}
        if not state.get(j).get(k):
            state[j][k] = {}

        state[j][k]["key"] = utils.client_key(state_key)
        state[j][k]["value"] = rio.get_val(state_key)
    
    
    return  render_template('html/state.html', state=state)


def container(rio, mp_id):
    s = "{}@container@{}@{}"
    ks = rio.get_keys(s.format(mp_id, "*", "title"))
    ret = []
    for k in sorted(ks):
        _, _, idx, _, _, _ = utils.parse_key(k)
        ret.append({"value_key": utils.client_key(k),
                    "ctrl_key": utils.client_key(s.format(mp_id, idx, "ctrl")),
                    "value":rio.get_val(k),
                    "idx": idx,
                    "link":"/{}/container/{}/state.html".format(mp_id, idx)})
    return ret

def definitions(rio, mp_id):
    s = "{}@definitions@{}@{}"
    ks = rio.get_keys(s.format(mp_id, "*","descr" ))
    ret = []
    for k in sorted(ks):
        _, _, idx, _, _, _ = utils.parse_key(k)
        ret.append({"value_key":utils.client_key(k),
                    "ctrl_key": utils.client_key(s.format(mp_id, idx, "ctrl")),
                    "value":rio.get_val(k),
                    "idx": idx,
                    "link":"/{}/definitions/{}/state.html".format(mp_id, idx)})
        
    return ret
