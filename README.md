# Info
- WebMidi to Jack bridge
- takes Midi Messages in form of simple json (e.g: ```[129,76,63]```)
  - midi msgs is a byte array of 3 bytes
- could be used in combination with my webmidikeyboard:
  - https://github.com/majorx234/webkeyboard

# Installation
- use venv & pip to installe dependencies
  - `python3 -m venv env`
  - `source env/bin/activate`
  - `pip install flask flask_cors flask_restx python-rtmidi`
  - or simple `pip install -r requirements.txt`

# Usage
- `python main.py`
