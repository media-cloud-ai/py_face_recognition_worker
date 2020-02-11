from setuptools import find_packages, setup
from ftv_facerec import __version__


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ftv_facerec',
    version=__version__,
    packages=find_packages(""),
    author="France Télévisions innovations et développement",
    author_email="mathia.haure-touze.ext@francetv.fr",
    description="Face recognition worker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "opencv-python>=4.2.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: MIT",
        "Operating System :: OS Independent",
    ]
 )
