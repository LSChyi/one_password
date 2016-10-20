# One Password
This is a simplified version of one password, user only need to remember one password, and generate different passwords for each service.

## Prebuild GUI App
There are some prebuild GUI apps from gui.py.

### OSX
[Download from NTU space](https://www.space.ntu.edu.tw/navigate/s/6E795D0812FC4AA9A3B6DF636F4E68A2QQY)  
This app is built from pyinstaller.

## How to use
There are two interfaces to use this project.

### Command line Interface (cli)

	pyton3 one_password.py
	
### GUI
![](img/gui screen shot.png)

	python3 gui.py

or double click the gui.py  
The GUI program will automatically copy password to your clipboard, so you can paste it easily **ctrl + v** or **command + v**

## Hash
This project use sha256 to hash the password and service you enter, then output as base64 string, for base64 contains upper cases, lower cases and numbers.

## License
This project is published under GPLv3.