"""define function below"""
def count(sequence, item):
    """function for counting items in sequence"""
    y = 0
    for n in sequence:
        if n == item:
            y+= 1
    return y
