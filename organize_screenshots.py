# Renan Greca, 2017
# This code is free to distribute and alter.

# Place this script in the same directory as the Switch's Album folder.
# View README.md for more details.
# More information: https://github.com/RenanGreca/Switch-Screenshots

import argparse
import json
import os
import sys
from collections import namedtuple
from shutil import copy2


# List of allowed extensions for files
ALLOWED_EXTENSIONS = [".jpg", ".jpeg", ".png", ".mp4"]
TIMESTAMP_LEN = 16
GAME_ID_LEN = 32
SWITCH_2_SUFFIX = "L"
SWITCH_1_LABEL = "Switch 1"
SWITCH_2_LABEL = "Switch 2"

# Argument parser
parser = argparse.ArgumentParser(description='''Nintendo Switch screenshot organizer.
                    Identifies images and creates new directory structure based on game title.
                    More information: https://github.com/RenanGreca/Switch-Screenshots''')
parser.add_argument('-i', '--input_dir', type=str, required=False, default='./Album/',
                    help='(str) Path to the Album directory. Default: ./Album/')
parser.add_argument('-o', '--output_dir', type=str, required=False, default='./Output/',
                    help='(str) Desired output directory. Default: ./Output/')
parser.add_argument('-j', '--json_file', type=str, required=False, default='./game_ids.json',
                    help='(str) JSON file containing the game IDs dictionary. Default: ./game_ids.json')
parser.add_argument('-s', '--split-consoles', action='store_true',
                    help='Place files under Switch 1/ and Switch 2/ subdirectories in the output folder.')


GameImage = namedtuple("GameImage", ("path", "timestamp", "game_id", "extension", "console"))

def parse_filename(name):
    stem, extension = os.path.splitext(name)
    if extension not in ALLOWED_EXTENSIONS:
        return None

    id_start = TIMESTAMP_LEN + 1
    id_end = id_start + GAME_ID_LEN
    if len(stem) < id_end or stem[TIMESTAMP_LEN] != '-':
        return None

    timestamp = stem[0:TIMESTAMP_LEN]
    base_id = stem[id_start:id_end]
    suffix = stem[id_end:]
    if suffix == SWITCH_2_SUFFIX:
        # Switch 2 IDs keep the trailing L so they match game_ids.json keys.
        console = SWITCH_2_LABEL
        game_id = base_id + SWITCH_2_SUFFIX
    elif suffix == '':
        console = SWITCH_1_LABEL
        game_id = base_id
    else:
        return None

    return GameImage(path=None, timestamp=timestamp, game_id=game_id, extension=extension, console=console)

def lookup_title(game_ids, game_id):
    if game_id in game_ids:
        return game_ids[game_id]
    # Fall back for older JSON entries that omit the Switch 2 L suffix.
    if game_id.endswith(SWITCH_2_SUFFIX):
        base_id = game_id[:-len(SWITCH_2_SUFFIX)]
        if base_id in game_ids:
            return game_ids[base_id]
    return None

def list_images(dir):
    r = []
    # Iterate over all files in the input directory
    for root, _, files in os.walk(dir):
        for name in files:
            game_image = parse_filename(name)
            if game_image is None:
                continue
            path = os.path.join(root, name)
            r.append(game_image._replace(path=path))
    return r


def organize_screenshots(game_ids, input_dir, output_dir, split_consoles=False):
    images = list_images(input_dir)
    count = len(images)

    not_found = dict()
    # Iterate over images
    for idx, image in enumerate(images):
        title = lookup_title(game_ids, image.game_id)
        if title is not None:
            # If the ID was in the JSON file, the directory is named with the title
            folder_name = title #.replace(':', '')
        else:
            folder_name = image.game_id
            not_found[image.game_id] = image.path

        # Create the directory and copy the file
        if split_consoles:
            path = os.path.join(output_dir, image.console, folder_name)
        else:
            path = os.path.join(output_dir, folder_name)
        if not os.path.exists(path):
            os.makedirs(path)
        copy2(image.path, path)

        # Print progress indicator
        sys.stdout.write("\r"+str(idx+1)+"/"+str(count))
        sys.stdout.flush()

    if len(not_found):
        # Print list of IDs that did not match any game
        print("\nNames not found for the following game IDs:")
        for game_id, path in not_found.items():
            print("\n"+game_id+"\nFound in: "+path)

if __name__ == '__main__':
    args = parser.parse_args()
    input_dir = args.input_dir
    output_dir = args.output_dir
    json_file = args.json_file

    # Load game IDs file
    with open(json_file) as data_file:
        game_ids = json.load(data_file)

    organize_screenshots(game_ids, input_dir, output_dir, args.split_consoles)
