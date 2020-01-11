props = {}
with open("/mc/server.properties") as f:
    for line in f:
        if line.startswith('#'):
            continue
        elif '=' not in line:
            continue
        else:
            k, v = line.split('=', 1)
            props[k.strip()] = v.strip()

worlds["world"] = "/mc/snapshot"

renders["overworld"] = {
    "world": "world",
    "title": "Overworld",
    "rendermode": smooth_lighting,
}

renders["nether"] = {
    "world": "world",
    "title": "Nether",
    "rendermode": nether_smooth_lighting,
    "dimension": "nether",
}

renders["end"] = {
    "world": "world",
    "title": "End",
    "rendermode": smooth_lighting,
    "dimension": "end",
}

outputdir = "/srv/overviewer"
texturepath = "/ov/client.jar"
imgformat = "webp"
