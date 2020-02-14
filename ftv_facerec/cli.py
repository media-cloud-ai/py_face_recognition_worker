import argparse
import json

def generate_parser():

    parser = argparse.ArgumentParser(
        description="Perform face recognition worker cli")
    parser.add_argument('source_path', type=str)
    parser.add_argument('persons_path', type=str)
    parser.add_argument('destination_path', type=str)
    parser.add_argument('provider_name', type=str)
    parser.add_argument('sample_rate', type=int)

    return parser