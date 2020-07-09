from flask import render_template
def state(rio, mp_id, struct, idx):
    state_keys = rio.get_keys("{}@{}@{}@state@*".format( mp_id, struct, idx))
    if not state_keys:
        return "404"
    for state_key in state_keys:
        print(state_key)
    template = 'html/index.html'
    return render_template(template, keys=state_keys)
