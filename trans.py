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

def title(rio, mp_id, struct, idx):
    s = "{}@{}@{}@{}"
    h = ""
    d = ""
    if struct == "container":
        h = "container {}: {}".format(idx,rio.get_val(s.format(mp_id, struct, idx, "title")))
        d = rio.get_val(s.format(mp_id, struct, idx, "descr"))
    if struct == "definitions":
        h = "definition class: {}".format(rio.get_val(s.format(mp_id, struct, idx, "class")))
        d = rio.get_val(s.format(mp_id, struct, idx, "descr"))
        
    return {"head":h,"sub":d}

def container(rio, mp_id):
    s = "{}@container@{}@{}"
    ks = rio.get_keys(s.format(mp_id, "*", "title"))
    ret = []
    for k in sorted(ks):
        _, _, idx, _, _, _ = utils.parse_key(k)
        ctrl_key = s.format(mp_id, idx, "ctrl")
        ret.append({"value_key": utils.client_key(k),
                    "ctrl_key": utils.client_key(ctrl_key),
                    "ctrl_value": utils.val_to_class(rio.get_val(ctrl_key)),
                    "value":rio.get_val(k),
                    "idx": idx,
                    "link":"/{}/container/{}".format(mp_id, idx)})
    return ret

def definitions(rio, mp_id):
    s = "{}@definitions@{}@{}"
    ks = rio.get_keys(s.format(mp_id, "*","descr" ))
    ret = []
    for k in sorted(ks):
        _, _, idx, _, _, _ = utils.parse_key(k)
        ctrl_key = s.format(mp_id, idx, "ctrl")
        ret.append({"value_key":utils.client_key(k),
                    "ctrl_key": utils.client_key(ctrl_key),
                    "ctrl_value": utils.val_to_class(rio.get_val(ctrl_key)),
                    "value":rio.get_val(k),
                    "idx": idx,
                    "link":"/{}/definitions/{}".format(mp_id, idx)})
        
    return ret
