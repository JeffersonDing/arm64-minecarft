# Setup Script for Native Apple Silicon Minecraft

Setup script for any version of Minecraft to run natively on Apple M1 family processers using the official launcher and official files.

## Versions Tested
- [x] 1.18.0
- [x] 1.18.1
- [x] 1.18.2

## Preparation
1. Install the official Minecraft Launcher from the Mojang website
2. Install a native Java JRE environment, using `homebrew` or [Azul Zulu JDK](https://www.azul.com/downloads/?package=jdk)
3. Install a version of Minecraft through the Minecraft Launcher, this will be in `Rosetta`


## Usage
1. Clone this repository to a convenient location
2. Type the following command and do not run it just yet
```shell
$ python3 setup.py
```
3. Locate your Minecraft installation folder, it's usually under `$HOME/Library/Application Support/minecraft`
4. Drag and drop the directory into the terminal, the command should look like this
```shell
$ python3 setup.py $HOME/Library/Application\ Support/minecraft
```
5. Run the script

## Launcher Setup
Once you have successfully ran the script, **relaunch** the Minecraft Launcher and click on installations.
1. Create a new installation and under versions, you should see a release named `<version>-arm`
2. Click on `More Options` and under `Java Executable` find the path to the native ARM Java binary, it's usually under `/usr/bin/java`. Run `which java` in your terminal to locate the binary if you don't know where it is.

## Performance
Tested on `MacBook Pro 14'` with a 10-core CPU and 16-core GPU, the framerate almost double from `40-60 fps` to a stable `90-110 fps`.

<img width="853" alt="Screen Shot 2022-04-07 at 4 33 20 PM" src="https://user-images.githubusercontent.com/51764604/162293766-a9fa1362-69bd-4f8f-90f7-9fb392580402.png">
<img width="852" alt="Screen Shot 2022-04-07 at 4 29 38 PM" src="https://user-images.githubusercontent.com/51764604/162293834-9d4d67d4-f3e6-43b3-bab2-e448f2de8447.png">



## Enjoy!
