import numpy as np
def convert_height(x):
    if isinstance(x, str):
        if "'" in x and '"' in x:
            feet, inches = x.split("'")
            inches = inches.replace('"', '')
            return round(int(feet) * 30.48 + int(inches) * 2.54)
        elif 'cm' in x:
            return int(x.replace('cm', ''))
    return x

def convert_weight(x):
    if isinstance(x, str):
        if "lbs" in x:
            return round(int(x.replace("lbs", "")) / 2.205)
        elif 'kg' in x:
            return int(x.replace('kg', ''))
    return x

def convert_money(x):
    if isinstance(x, str):
        x = x.replace('€', '')
        if 'M' in x: return float(x.replace('M', '')) * 1_000_000
        elif 'K' in x: return float(x.replace('K', '')) * 1_000
        return float(x)
    return x

def convert_hits(x):
    if isinstance(x, str):
        x = x.strip()
        if 'K' in x: return float(x.replace('K', '')) * 1000
        return float(x)
    return x
