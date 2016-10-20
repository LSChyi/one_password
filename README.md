# One Password
This is a simplified version of one password, user only need to remember one password, and generate different passwords for each service.

## How to use
There are two interfaces to use this project.

### Command line Interface (cli)

	pyton3 one_password.py
	
### GUI

	python3 gui.py

or double click the gui.py  
The GUI program will automatically copy password to your clipboard, so you can paste it easily **ctrl + v** or **command + v**

## Hash
This project use sha256 to hash the password and service you enter, then output as base64 string, for base64 contains upper cases, lower cases and numbers.

## License
This project is published under GPLv3.