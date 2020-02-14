import datetime
import json
import os
import multiprocessing
import cv2
import tqdm
import logging
logging.basicConfig(level=logging.DEBUG)

from ftv_facerec import providers, utils, cli

images_path = "./data"

def analyze_video(source_path, persons_path, destination_path, provider_name, sample_rate):

    if not hasattr(providers, provider_name):
        logging.error("Unavailable provider: {0:s}".format(provider_name))

    pattern = "{destination_path:s}/{source_filename:s}_analyzed.json"

    # Prepare output
    output_json = {"frames":[]}
    output_json_path = pattern.format(
        destination_path = destination_path,
        source_filename = os.path.splitext(
            os.path.basename(source_path)
        )[0]
    )

    # Prepare provider
    provider_class = eval(
        "providers.{provider_name}".format(
            provider_name = provider_name))
    provider = provider_class()

    # Prepare images
    with open(persons_path, 'r') as fp:
        persons_json =  json.load(fp)
    utils.prepare_images(persons_json["persons"], images_path)

    # Train model
    provider.train("{0}/*".format(images_path))

    # Open video capture
    input_movie = cv2.VideoCapture(source_path)
    length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

    # Recognize faces on video
    with multiprocessing.Pool() as pool:
        for frame_json in tqdm.tqdm(
            pool.imap(
                provider.recognize, 
                utils.iter_by_image(input_movie)
            ), 
            total=length):
            output_json["frames"].append(frame_json)

    with open(output_json_path, "w") as f:
        f.write(json.dumps(output_json))


def main():
    parser = cli.generate_parser()
    parameters = parser.parse_args()
    analyze_video(**vars(parameters))