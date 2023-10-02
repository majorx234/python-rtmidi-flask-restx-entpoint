from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from environment import config
import logging
from resources.midi_endpoint import api as midi_endpoint_api_namespace

app = Flask("Midi Endpoint")

CORS(app)

api = Api(app,
          version='0.1',
          title='Midi Endpoint',
          description='a web service to receive MIDI data',
#          doc=config.documentation_path
          doc='/swagger-ui'
          )

api.add_namespace(midi_endpoint_api_namespace)

if __name__ == '__main__':
    logging.basicConfig(filename=config.log_path, level=logging.DEBUG)
    logging.info("start midi endpoint service")

    app.run(debug=config.debug, port=config.port, host= '0.0.0.0')
