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

worlds["Overworld"] = "/mc/snapshot"
worlds["Nether"] = "/mc/snapshot"
worlds["End"] = "/mc/snapshot"

renders["overworld_day"] = {
    "world": "Overworld",
    "title": "Daytime",
    "rendermode": smooth_lighting,
}

renders['overworld_night'] = {
    'world': 'Overworld',
    'title': "Nighttime",
    'rendermode': smooth_night,
}

renders["nether"] = {
    "world": "Nether",
    "title": "Nethertime",
    "rendermode": nether_smooth_lighting,
    "dimension": "nether",
}

renders["end"] = {
    "world": "End",
    "title": "Endtime",
    "rendermode": smooth_lighting,
    "dimension": "end",
}

outputdir = "/srv/overviewer"
texturepath = "/ov/client.jar"
imgformat = "webp"
