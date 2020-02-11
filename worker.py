import ftv_facerec


def get_name():
    return "Face recognition worker"


def get_short_description():
    return "Process face recognition on a video"


def get_description():
    return """Retrieve a json file from an video.
        The input requires:
        - a video
        """


def get_version():
    return ftv_facerec.__version__


def get_parameters():
    return [
        {
            "identifier": "source_path",
            "label": "Source Path",
            "kind": ["string"]
        },
        {
            "identifier": "destination_path",
            "label": "Destination Path",
            "kind": ["string"]
        }
    ]


def process(parameters):
    return
