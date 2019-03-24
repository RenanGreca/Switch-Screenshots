# Renan Greca, 2017
# This code is free to distribute and alter.

# Place this script in the same directory as the Switch's Album folder.
# View README.md for more details.
# More information: https://github.com/RenanGreca/Switch-Screenshots

import os
import json
from shutil import copy2
import argparse
import sys

# Argument parser
parser = argparse.ArgumentParser(description='''Nintendo Switch screenshot organizer. 
                    Identifies images and creates new directory structure based on game title. 
                    More information: https://github.com/RenanGreca/Switch-Screenshots''')
parser.add_argument('-i', '--input_dir', type=str, required=False, default='./Album/',
                    help='(str) Path to the Album directory. Default: ./Album/')
parser.add_argument('-o', '--output_dir', type=str, required=False, default='./Output/',
                    help='(str) Desired output directory. Default: ./Output/')

# Create a list of all the image/video files in the Album directory.
# Thanks to L. Teder
# https://stackoverflow.com/a/36898903
def list_images(dir):
    r = []
    for root, _, files in os.walk(dir):
        for name in files:
            if "jpg" in name or "mp4" in name or "png" in name:
                r.append(os.path.join(root, name))
    return r

def organize_screenshots(game_ids, input_dir, output_dir):
    images = list_images(input_dir)
    count = len(images)

    not_found = []
    # Iterate over images
    for idx, image in enumerate(images):
        # Split the filename to find the game ID
        image_id = image.split('-')[1].split('.')[0]
        
        if image_id in game_ids:
            # If the ID was in the JSON file, create a directory using the game's title and copy the file
            game_title = game_ids[image_id]
            path = os.path.join(output_dir, game_title)
            if not os.path.exists(path):
                os.makedirs(path)
            copy2(image, path)
        else:
            # Otherwise, create a directory using the game's ID
            not_found.append(image)
            path = os.path.join(output_dir, image_id)
            if not os.path.exists(path):
                os.makedirs(path)
            copy2(image, path)

        # Print progress indicator
        sys.stdout.write("\r"+str(idx+1)+"/"+str(count))
        sys.stdout.flush()

    if len(not_found):
        print("\nGame IDs not found for the following files:")
        print("\n".join(not_found))

if __name__ == '__main__':
    args = parser.parse_args()
    input_dir = args.input_dir
    output_dir = args.output_dir

    # Load game IDs file
    with open('game_ids.json') as data_file:
        game_ids = json.load(data_file)
    
    organize_screenshots(game_ids, input_dir, output_dir)