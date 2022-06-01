# DDLC Comfy UI
<img src="Logo.png?raw=true">

---
Hey, I'm no writer, so just skip to the **Features** section, okay?



## Features
* Multiple UI themes
* In-game theme configurator
* HiDPI support



## Compatibility
You'll be good to go with pretty much every mod that doesn't try to change the UI.

The verified ones are:
* Doki Doki Literature Club
* Monika After Story
* Monika Before Story
* Purist



## Screenshots
<table>
  <tr>
    <th></th>
    <th>Normal</th>
    <th>Dark</th>
  <tr>
    <td>Unmodded</td>
    <td><img src="Screenshots/Unmodded.png?raw=true" width="320"></td>
    <td><img src="Screenshots/UnmoddedDark.png?raw=true" width="320"></td>
  </tr>
  <tr>
    <td>Default</td>
    <td><img src="Screenshots/Default.png?raw=true" width="320"></td>
    <td><img src="Screenshots/DefaultDark.png?raw=true" width="320"></td>
  </tr>
  <tr>
    <td>Cold</td>
    <td><img src="Screenshots/Cold.png?raw=true" width="320"></td>
    <td><img src="Screenshots/ColdDark.png?raw=true" width="320"></td>
  </tr>
  <tr>
    <td>Mint</td>
    <td><img src="Screenshots/Mint.png?raw=true" width="320"></td>
    <td><img src="Screenshots/MintDark.png?raw=true" width="320"></td>
  </tr>
  <tr>
    <td>Peach</td>
    <td><img src="Screenshots/Peach.png?raw=true" width="320"></td>
    <td><img src="Screenshots/PeachDark.png?raw=true" width="320"></td>
  </tr>
  <tr>
    <td>Strawberry</td>
    <td><img src="Screenshots/Strawberry.png?raw=true" width="320"></td>
    <td><img src="Screenshots/StrawberryDark.png?raw=true" width="320"></td>
  </tr>
  <tr>
    <td>Classic</td>
    <td><img src="Screenshots/Classic.png?raw=true" width="320"></td>
    <td><img src="Screenshots/ClassicDark.png?raw=true" width="320"></td>
  </tr>
  <tr>
    <td>Mystique</td>
    <td><img src="Screenshots/Mystique.png?raw=true" width="320"></td>
    <td><img src="Screenshots/MystiqueDark.png?raw=true" width="320"></td>
  </tr>
  <tr>
    <td>Chocolate</td>
    <td><img src="Screenshots/Chocolate.png?raw=true" width="320"></td>
    <td><img src="Screenshots/ChocolateDark.png?raw=true" width="320"></td>
  </tr>
  <tr>
    <td>Starry</td>
    <td><img src="Screenshots/Starry.png?raw=true" width="320"></td>
    <td><img src="Screenshots/StarryDark.png?raw=true" width="320"></td>
  </tr>
</table>



## Installation
1. Download the latest release archive: [for DDLC](https://github.com/Iniquitatis/DDLCComfyUI/releases/download/v2.0.1/DDLCComfyUI_v2.0.1.zip) or [for MAS](https://github.com/Iniquitatis/DDLCComfyUI/releases/download/v2.0.1/MASComfyUI_v2.0.1.zip)
2. Extract the contents of the archive to the `game` subdirectory of the DDLC installation directory



## Usage
1. Launch the game
2. Go to the **Settings** screen (**Submods** in MAS)
3. Navigate to the mod section
4. Select a theme by moving a slider underneath the **Theme** label
    * Uncheck the **Fonts** checkbox to disable the new fonts
    * Uncheck the **Layout** checkbox to disable the layout changes
    * Check the **HiDPI** checkbox if the high resolution UI assets are needed
5. Press **Apply** and restart the game



## Uninstallation
1. Launch the game
2. Go to the **Settings** screen (**Submods** in MAS)
3. Navigate to the mod section
4. Press **Disable** and close the game
5. Remove the following entries from the DDLC installation directory:
    * `game/comfy_meta/` (*directory*)
    * `game/comfy_ui/` (*directory*)
    * `game/comfy_ui.rpy`
    * `game/comfy_ui.rpyc`
    * `game/python-packages/comfy_ui.py`



## Troubleshooting
If the mod doesn't work after the installation and gives you a traceback:
1. Make sure you downloaded the correct archive (see [Installation](#installation) for links).
    * The `MASComfyUI_vX.X.X.zip` archive won't work on a pure DDLC installation.
    * The `DDLCComfyUI_vX.X.X.zip` archive won't work on a MAS-modded game.
    * The archive should contain:
        * `python-packages`
        * `comfy_ui.rpy`
        * ...
    * The archive should **not** contain:
        * `Source`
        * `Make.py`
        * ...
2. Make sure you unpacked the archive into the correct directory.
    * **IMPORTANT:** For MAS users, I have to emphasize that this mod should **not** be installed into the `Submods` directory.
    * The simplest method to check if the mod is installed correctly is to see if the `game` directory contains:
        * `comfy_meta`
        * `comfy_ui`
        * `comfy_ui.rpy`
    * Example of file which will be present in the installed mod:
        * **CORRECT:** `C:\Program Files (x86)\Steam\steamapps\Doki Doki Literature Club\game\comfy_ui.rpy`
        * **INCORRECT:** `C:\Program Files (x86)\Steam\steamapps\Doki Doki Literature Club\game\Submods\MASComfyUI_v2.0.1\comfy_ui.rpy`
3. Make sure you're using the latest version available (see the [Releases](https://github.com/Iniquitatis/DDLCComfyUI/releases) section on the GitHub project page).

If none of the above works, feel free to open an issue ticket.



## FAQ
Let's pretend that you've already asked a couple of questions.

**Q:** Why?  
**A:** Because I can.

**Q:** It looks out of place.  
**A:** Well, you're outside the target audience. Sorry.



## Known Bugs
None at the moment.



## Special Thanks
Dan Salvato and Team Salvato respectively.



## License
See LICENSE file in the root of this repository.
