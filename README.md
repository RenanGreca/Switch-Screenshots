# Nintendo Switch Screenshot Organizer
Script to organize Nintendo Switch screenshots by game title instead of date.

Written by Renan Greca in 2017.
This code is free to distribute and alter.

## Download
The latest stable release is 2.0.0. Download the Python file (Mac or Linux) or the Windows executable here:

https://github.com/RenanGreca/Switch-Screenshots/releases/tag/v1.2.0

You also need the `game_ids.json` file from the most recent release.
This file is updated as we discover new IDs for games.

https://github.com/RenanGreca/Switch-Screenshots/releases

## Usage
Place the program and the `game_ids.json` file in the same directory as the
Switch's Album folder, either on the microSD card or on your computer after
transferring the Album.

After running, all screenshots will be placed within directories according to
which game they are from. They can be found within the Output directory.

If the game is currently not in the IDs file, a folder will be created using 
the game ID instead of title. You can rename it but please contribute the ID
to the repository by filing an issue or pull request.

### Windows
Double-click `organize_screenshots.exe`.

### macOS
On a terminal, run:
```
python organize_screenshots.py
```

### Linux
On a terminal, run:
```
python organize_screenshots.py
```

#### Optional parameters:

* `-i INPUT_DIR`: Specifies location of the Album directory. Default: `./Album/`.
* `-o OUTPUT_DIR`: Specifies desired output directory. Default: `./Output/`.

## About the game IDs

Switch screenshots are stored in the following format: `[timestamp]-[game id].jpg`.
Therefore, we can use the filenames to figure out from which game it was taken.

For example, the screenshot `2017030619573600-F1C11A22FAEE3B82F21B330E1B786A39.jpg`
was taken on March 6, 2017 in the game The Legend of Zelda: Breath of the Wild.
Some titles may have more than one ID, depending on the region or version. Demos
also have their own IDs.

The Switch UI contains multiple IDs, for different parts of the UI (home menu,
friends list, system settings, etc.). For simplicity, I've labeled all those
IDs as "Nintendo Switch".

Today, the Switch saves files as JPG (screenshots) or MP4 (recordings). The program
also supports PNG files in case Nintendo ever adds lossless screenshots.

The `game_ids.json` file follows this format:
```
{
  "F1C11A22FAEE3B82F21B330E1B786A39": "The Legend of Zelda Breath of the Wild",
  "16851BE00BC6068871FE49D98876D6C5": "Mario Kart 8 Deluxe"
}
```

**Important**: If the game's title includes a colon (`:`), please remove it, as
this character is not allowed in file or directory names.

## Contributing

The initial version of `game_ids.json` contained only the titles I have played.
If you have a screenshot for a game that is not on this list, the program will
output a warning telling you which screenshot it was.

You may manually add the ID to the `game_ids.json` file, but it would be greatly
appreciated if you could submit an issue request on GitHub detailing the ID
that was not found and which game and region the screenshot is from.

The Windows `.exe` was generated using PyInstaller.

## Discussion

If you want to discuss the program or ask questions about it, create an issue, check out the 
[Reddit thread at /r/NintendoSwitch](https://www.reddit.com/r/NintendoSwitch/comments/6rcttl/i_made_a_program_to_organize_switch_screenshots/) 
or send me a tweet [@RenanGreca](https://twitter.com/RenanGreca). :)
