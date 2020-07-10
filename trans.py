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

        state[j][k] = rio.get_val(state_key)

    return  ## render template --> jsonify(state)
