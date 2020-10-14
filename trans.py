from flask import render_template
import utils
import json

def build_val_dict(rio, keys, parse=False):
    val ={}
    for key in keys:
        _, _, _, _, j, k = utils.parse_key(key)
        if not val.get(j):
            val[j] = {}
        if not val.get(j).get(k):
            val[j][k] = {}

        val[j][k]["key"] = utils.client_key(key)
        v = rio.get_val(key)
        if parse:
            v = json.loads(v)
        val[j][k]["value"] = v

    return val

def content_html(rio, mp_id, struct, idx):
    state_keys = rio.get_keys("{}@{}@{}@state@*".format( mp_id, struct, idx))
    definition_keys = rio.get_keys("{}@{}@{}@definition@*".format( mp_id, struct, idx))

    if not state_keys:
        return "404"

    state = build_val_dict(rio, state_keys)
    definition = build_val_dict(rio, definition_keys, True)

    return  render_template('html/content.html', state=state, definition=definition)

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
