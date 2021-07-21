from flask_restx import Namespace, Resource
from flask import Flask, jsonify, request
from http import HTTPStatus
import rtmidi

status = "ok"
midi_msg = [0x80, 60, 0]
midiout = rtmidi.MidiOut(rtapi=rtmidi.API_UNIX_JACK)
rtMidiOutputPorts = midiout.get_ports()
if rtMidiOutputPorts:
    midiout.open_port(0)

api = Namespace('midi_endpoint', description='game_ratings related operations')

# www.laurasserver.de/midi_endpoint/
# crud create read update delete: (POST,GET,PUT,DELETE) PGPD


@api.route('')
class MidiEndpoint(Resource):
#    def __init__(self):
#        self.midi_msg = [0x80, 60, 0]
#        self.midiout = rtmidi.MidiOut(rtapi=rtmidi.API_UNIX_JACK)    
#        self.rtMidiOutputPorts = self.midiout.get_ports()

#    def get(self):
#        ''' send status '''
#        return status, HTTPStatus.OK

    def post(self):
        '''Adds a game to games'''
        midi_msg_raw = request.json
        print(midi_msg_raw)
        midi_msg = [int(midi_msg_raw['status']),
                    int(midi_msg_raw['data1']),
                    int(midi_msg_raw['data2'])]
        midiout.send_message(midi_msg)
        return status, HTTPStatus.CREATED
