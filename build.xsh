import importlib.metadata
import json
import tarfile
import urllib.request


import numpy, PIL  # noqa


def get_json(url):
    with urllib.request.urlopen(url) as resp:
        return json.load(resp)


# Get pillow version
pillow_version = importlib.metadata.version('Pillow')

metadata = get_json("https://pypi.org/pypi/Pillow/json")
files = [f for f in metadata['releases'][pillow_version] if f['packagetype'] == 'sdist']
assert len(files) == 1

file_url = files[0]['url']
with urllib.request.urlopen(file_url) as sdist, tarfile.open(fileobj=sdist, mode='r|*') as tf:
    tf.extractall('/tmp')

$PIL_INCLUDE_DIR = pg`/tmp/Pillow-*/src/libImaging`[0]

python ./setup.py bdist_wheel
