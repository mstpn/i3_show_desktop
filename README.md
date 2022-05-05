# i3_show_desktop

Hide your current workspaces and show the desktop in [i3wm](https://i3wm.org/).  

## Installation

1. Clone the repository into your i3 configuration folder

```
mkdir -p ~/.config/i3/test
cd ~/.config/i3/test
git clone https://github.com/mstpn/i3_show_desktop.git
```

2. Modify your [i3 config file](https://i3wm.org/docs/userguide.html#configuring)  

```
nano ~/.config/i3/config
```
Append the following lines

```
#Show/hide desktop ($mod + Shift + d)                                                                                   
bindsym $mod+Shift+d exec python ~/.config/i3/i3_show_desktop/bg.py 
```
Reload the i3 config with the keybinding `$mod + Shift + r` or via the shell with

```
i3-msg reload
```

## Usage

The keybinding to toggle the desktop is `$mod + Shift + d`

## Limitations

This has only been tested on Arch Linux 5.17.5-arch1-1 using Python 3.10.4.

## License

i3_show_desktop is released under the [MIT License](https://opensource.org/licenses/MIT).
