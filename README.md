# Setup Script for Native Apple Silicon Minecraft

## Preparation
1. Install the official Minecraft Launcher from the Mojang website
2. Install a native Java JRE environment, using `homebrew` or [Azul Zulu JDK](https://www.azul.com/downloads/?package=jdk)
3. Install a version of Minecraft through the Minecraft Launcher, this will be in `Rosetta`


## Usage
1. Clone this repository to a convenient location
2. Type the following command and do not run it just yet
```
python3 setup.py
```
3. Locate your Minecraft installation folder, it's usually under `/Users/<USERNAME>/Library/Application Support/minecraft`
4. Drag and drop the directory into the terminal, the command should look like this
```
python3 setup.py /Users/<USERNAME>/Library/Application Support/minecraft/assets
```
5. Run the script

## Launcher Setup
Once you have successfully ran the script, **relaunch** the Minecraft Launcher and click on installations.
1. Create a new installation and under versions, you should see a release named `<version>-arm`
2. Click on `More Options` and under `Java Executable` find the path to the native ARM Java binary, it's usually under `/usr/bin/java`

## Enjoy!
