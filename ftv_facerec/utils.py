import face_recognition
import cv2
import requests
import shutil
import os

def get_writer_video(video_capture, output_path):
    """Create a video writer from a video capture

    Parameters
    ----------
    input_path : cv2.VideoCapture
        Path to the video
    output_path : str
        Path where to write 
    
    Returns
    -------
    cv2.VideoWriter
        Video Writer object
    """

    frame_size = (
        video_capture.get(cv2.CAP_PROP_FRAME_WIDTH),
        video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    )

    fps = video_capture.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter(
        output_path, fourcc, fps, frame_size)

    return video_writer

def iter_by_image(video_capture, sample_rate=1):
    """Iter by image over a cv2.VideoCapture object
    
    Parameters
    ----------
    video_capture : cv2.VideoCapture
        VideoCapture object representing a video
    sample_rate : int, optional
        Batch size, by default 128
    
    Yields
    -------
    list
        list of numpy array, each representing a frame
    """
    length = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

    for frame_number in range(0, length, sample_rate):
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Sample image
        if ret and frame_number%sample_rate == 0:
            yield frame, frame_number
        elif ret and not frame_number%sample_rate == 0:
            continue
        else:
            break

def prepare_images(persons, images_path):
    """Download and or
    
    Parameters
    ----------
    persons : dict
        List of dictionnaries each representing a person
    """

    pattern = "{images_path:s}/{person_name:s}_{id:d}{extension:s}"

    for person in persons:
        for id, url in enumerate(person["urls"]):
            image_path = pattern.format(
                images_path = images_path,
                person_name = person["name"],
                id = id,
                extension = os.path.splitext(url)[1]
            )
            download_image(url, image_path)

def download_image(image_url, image_path):
    """Download image from url and copy it to a path
    
    Parameters
    ----------
    image_url : str
        Image url source
    image_path : str
        Image path destination
    """
    resp = requests.get(image_url, stream=True)

    with open(image_path, 'wb') as image_file:

        shutil.copyfileobj(resp.raw, image_file)
    
    del resp