from flask import render_template
def state(rio, mp_id, struct, idx):
    state_keys = rio.get_keys("{}@{}@{}@state@*".format( mp_id, struct, idx))
    
    
    template = 'html/index.html'
    return render_template(template, keys=state_keys)
