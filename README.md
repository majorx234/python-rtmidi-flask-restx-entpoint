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

# REST Protocol
- post simple Midi messgaes to endpoint `midi_endpoint`
- messages need format: `{"status":"127","data1":"<note_value>","data2":"<intensity>"}`
  - `status`: note_on/note_off (128 or 144)
  - `data1`: <note_value> (0..127)
  - `data2`: <intensity> (0..127)

# Tests
- test Endpoint with:
  - `curl -H "Content-Type: application/json" --request POST -d '{"status":"127","data1":"61","data2":"00"}' "http://ros-arion-linux.local:5000/midi_endpoint"`
