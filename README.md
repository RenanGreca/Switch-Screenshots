# Nintendo Switch Screenshot Organizer
Script to organize Nintendo Switch screenshots by game title instead of date.

Written by Renan Greca in 2017.
This code is free to distribute and alter.

## Usage
Place this script in the same directory as the Switch's Album folder, either on
the microSD card or on your computer after transferring the Album.

On a terminal or command prompt, run:
```
python organize_screenshots.py
```

## About the game IDs

Switch screenshots are stored in the following format: `[timestamp]-[game id].jpg`.
Therefore, we can use the filenames to figure out which game it was from.

For example, the screenshot `2017030619573600-F1C11A22FAEE3B82F21B330E1B786A39.jpg`
was taken on March 6, 2017 in the game The Legend of Zelda: Breath of the Wild.
Some titles may have more than one ID, depending on the region or version. Demos
also have their own IDs.

The Switch UI contains multiple IDs, for different parts of the UI (home menu,
  friends list, system settings, etc.). For simplicity, I've labeled all those
  IDs as "Nintendo Switch".

The `game_ids.json` file follows this format:
```
{
  "F1C11A22FAEE3B82F21B330E1B786A39": "The Legend of Zelda Breath of the Wild",
  "16851BE00BC6068871FE49D98876D6C5": "Mario Kart 8 Deluxe"
}
```

## Contributing

The initial version of `game_ids.json` contains only the titles I have played.
If you have a screenshot for a game that is not on this list, the program will
output a warning telling you which screenshot it was.

You may manually add the ID to the `game_ids.json` file, but it would be greatly
appreciated if you could submit an issue request on GitHub detailing the ID
that was not found and which game and region the screenshot is from.
