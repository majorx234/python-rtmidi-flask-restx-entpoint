from flask_restx import Namespace, Resource
from flask import Flask, jsonify, request
from http import HTTPStatus
import rtmidi


api = Namespace('midi_endpoint',
                 description='game_ratings related operations')

#www.laurasserver.de/midi_endpoint/
# crud create read update delete: (POST,GET,PUT,DELETE) PGPD

@api.route('')
class MidiEndpoint(Resource):
    def __init__(self):
        self.midi_msg = [0x80, 60, 0]
        self.midiout = rtmidi.MidiOut(rtapi=rtmidi.API_UNIX_JACK)    
        self.rtMidiOutputPorts = midiout.get_ports()

    def get(self):
        ''' send status '''
        return status, HTTPStatus.OK

    def post(self):
        '''Adds a game to games'''
        midi_msg_raw = request.json
        print(midi_msg_raw)
        midi_msg = [midi_msg_raw['status']
        midiout.send(midi_msg)
        return midi_msg, HTTPStatus.CREATED
