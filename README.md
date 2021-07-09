# shazamTelegramBot

Bot for Telegram messenger that works similarly to Shazam application: it replies to audio and voice messages containing sample of a song with it's title and subtiltle, plus a link to this song on Apple Music 


## Project Screen Shots

![A song recongized](screenshots/Screenshot_1.png?raw=true "A song recongized")

![Another song recongized](screenshots/Screenshot_2.png?raw=true "Another song recongized")

## Installation and Setup Instructions

Clone down this repository. Make sure Python3.6+ is installed on your machine, then, in terminal, `cd` to the cloned repository, create and activate `venv`.

Now, install required packages using
`pip install requirements.txt`

To run this this bot you also need to have `ffmpeg` installed and added to PATH **before** creating `venv`

Create a new Telegram bot using @BotFather, name it as you wish, then copy the recieved `Bot API Token` to file named `TOKEN`

Now to run the application simply execute 
`python main.py`
