from __future__ import absolute_import

import face_recognition
import glob
import os
import numpy as np

from ftv_facerec.providers.base_provider import BaseProvider

class FaceRecognitionProvider(BaseProvider):
    def __init__(self):
        super().__init__()
        self.known_faces = []
        self.known_names = []

    def train(self, path_pattern, recursive=False):
        """[summary]
        
        Parameters
        ----------
        path_pattern : str
            Glob path pattern
        recursive : bool, optional
            Glob recursive option, by default False
        """
        self.known_faces = []
        self.known_names = []

        for filename in glob.glob(path_pattern, recursive=recursive):

            image = face_recognition.load_image_file(filename)
            self.known_faces.append(face_recognition.face_encodings(image)[0])
            self.known_names.append(os.path.basename(filename))

    def recognize(self, frame_data):

        frame, frame_number = frame_data
        
        # Initialize some variables
        face_locations = []
        face_encodings = []

        # Output
        frame_json = {
            "id" : frame_number,
            "people": []
        }

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for the known face(s)
            distances = face_recognition.face_distance(self.known_faces, face_encoding)

            name = self.known_names[np.argmin(distances)]
            distance = min(distances)

            frame_json["people"].append({
                "name": name,
                "distance": distance,
                "trbl": [top, right, bottom, left]
            })
        
        return frame_json