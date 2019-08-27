


def euclideanAlgo(upper,lower):
    
    while (upper % lower) > 0:
       remander = upper % lower
       upper=lower
       lower = remander
    return lower
