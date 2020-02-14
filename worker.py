import ftv_facerec
import logging

logging.basicConfig(level=logging.ERROR)

def get_name():
    return ftv_facerec.name


def get_short_description():
    return ftv_facerec.short_description


def get_description():
    return ftv_facerec.description


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
            "identifier": "persons_path",
            "label": "Json file representing person to detect",
            "kind": ["object"]
        },
        {
            "identifier": "destination_path",
            "label": "Destination Path",
            "kind": ["string"]
        },
        {
            "identifier": "provider",
            "label": "Provider name",
            "kind": ["string"]
        },
        {
            "identifier": "sample_rate",
            "label": "Specify the rate of analysed frame",
            "kind": ["integer"]
        },

    ]


def process(parameters):
    return