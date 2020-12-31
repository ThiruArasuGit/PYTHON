fileName = 'config.properties'
params = {}

def configProps():
    fobj = open(fileName)
    for line in fobj:
        line = line.strip()
        if not line.startswith("#"):
            key_value = line.split("=")
            if len(key_value) == 2:
                params[key_value[0].strip()] = key_value[1].strip()
    return params


