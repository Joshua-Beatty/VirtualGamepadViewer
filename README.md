# Virtual Gamepad Viewer
Monitors keyboard inputs and visualizes a virtual gamepad for stream overlays

## Getting started
Needed python libraries run GamepadVisualizer.py:
> os, sys, glob, pickle, tkinter, pygame, keyboard



To run the VirtualGamepadViewer python script do
```bash
python VirtualGamepadViewer.py
```
### To build
Needed python libraries to build VirtualGamepadViewer.py:
> os, sys, glob, pickle, tkinter, pygame, keyboard, cx_Freeze

Build the program using the included build.py

```bash
python build.py build
```
This will build to
> ./build/name-of-build-type/

Then run 
> VirtualGamepadViewer.exe

## Usage
Right click on the screen to select a new a skin

Middle click on the screen to enable printing of every currently pressed keycode 
for the use of debugging/creating new skins

### Skins
A skin is simply a folder that contains at least a background.png file.

This skin on its own would do nothing but display the background. Any additional .png files will be parsed and displayed based off of its name. A file called 30.png or a.png will be displayed if the `A` button is pressed. A "+" symbol would signify that two keycodes surrounding the "+" must be pressed down at the same time. A "-" signify that it will activate if either keycode on the sides of it is pressed. Both "+" and "-" can be chained together, but "-" is always above "+" in the hierarchy.

#### Keycodes
Keycodes are grabbed from the [python keyboard library](https://github.com/boppreh/keyboard). 

This means that keycodes are in the format of letters or names or as keycodes. They can be used interchangeably.

#### Examples
` 30 is the keycode for a `

>a.png

Will be displayed if the `A` button is being held down

> 30+s.png

Will be displayed only if the `A` button and the `S` button are being held down

> a-s.png

Will be displayed if either the `A` button or the `S` button is being held down

> 30-s+d.png

Will be displayed if either the `A` button is being held down or the `S` button and `D` button are being held down

## Trouble Shooting

#### The skin I chose has a background that is too small and now I can't select another skin
Either delete the save.p file and relaunch or modify the background.png file and relaunch.

#### I want my skin to be able to show only if X is pressed and then if either Y or Z is pressed
If you want keycodes (1 or 2) and 3 to be pressed, you must distribute the and so the file name would be
> 1+3-2+3.png
## License
[Polyform Noncommercial License 1.0.0](./LICENSE)
