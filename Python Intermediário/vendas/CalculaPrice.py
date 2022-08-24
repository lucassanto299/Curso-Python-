from vendas.formata.price import realbr
def increase(value, percentage, formata=False):
    r = (value + (value * (percentage / 100)))
    if formata is not False:
        return realbr(r)

def reduction(value, percentage, formata=False):
    r = (value - (value * (percentage / 100)))
    if formata is not False:
        return realbr(r)