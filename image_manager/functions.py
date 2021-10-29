from os import path
import requests
import shutil

def download_image(image_url: str, output_dir: str) -> None:
    name = image_url.split("/")[-1]
    filename = path.join(output_dir, name)

    r = requests.get(image_url, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True

        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    else:
        #throw new Exception
        pass
