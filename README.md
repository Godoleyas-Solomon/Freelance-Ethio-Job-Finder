# Freelance-Ethio-Job-Finder
This project is made for the sole purpose of getting new job posting from the telegram channel @freelance_ethio and filtering out your preferred job and forwarding it to your private chat.

## Dependencies
This python script requires this dependencies to be installed
```
poe-api
telethon
```

## Usage
```
bash
git clone https://github.com/Godoleyas-Solomon/Freelance-Ethio-Job-Finder.git
cd Freelance-Ethio-Job-Finder
pip install -r requirements.txt
cp sampleconfig.py config.py

___ config.py ___
api_id = your api id(int)
api_hash = your api hash(str)
channel = 'freelance_ethio'
dump = your chat(str if it is a username and int if it is an id)
cookie = poe.com p-b cookie get it from chromiun>poe.com>application>p-b key
AI = type of AI (choose from down below)
You can change the prompt as you see fit.
```
AI list
```
"a2": "Claude-instant",
"capybara": "Assistant",
"chinchilla": "ChatGPT"
```

When you are done simply execute
```
python app.py
```
