from os import path
import requests
import shutil


def download_image(image_url: str, output_dir: str, name='') -> str:
    extension = image_url.split('.')[-1]
    if name == '':
        name = image_url.split("/")[-1]
    else:
        if extension not in name:
            name = name + '.' + extension

    filename = path.join(output_dir, name)

    r = requests.get(image_url, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True

        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        return filename
    else:
        return None
