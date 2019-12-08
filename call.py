import os
import bottle
from bottle import route, run, post, Response
from twilio import twiml
from twilio.rest import Client

app = bottle.default_app()

account = "AC07ba3e67248d268548ae6e1ee9fcf73f"
token = "24c80b200aff3f8cdf4a69b43da5bf62"

client = Client(account, token)

# input your Twilio number in the second string on the next line
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER', '+13395269065')
NGROK_BASE_URL = os.environ.get('http://7b8659ac.ngrok.io/', '')


@route('/')
def index():
    """Returns standard text response to show app is working."""
    return Response("Bottle app up and running!")


@post('/twiml')
def twiml_response():
    """Provides TwiML instructions in response to a Twilio POST webhook
    event so that Twilio knows how to handle the outbound phone call
    when someone picks up the phone.
    """
    response = VoiceResponse()
    response.say("Hello, this call is from a Bottle web application.")
    response.play("https://api.twilio.com/cowbell.mp3", loop=10)
    return str(response)


@route('/dial-phone/<outbound_phone_number>')
def outbound_call(outbound_phone_number):
    """Uses the Twilio Python helper library to send a POST request to
    Twilio telling it to dial an outbound phone call from our
    specific Twilio phone number (that phone number must be owned by our
    Twilio account).
    """
    # the url must match the Ngrok Forwarding URL plus the route defined in
    # the previous function that responds with TwiML instructions
    client.calls.create(to=outbound_phone_number,
                               from_=TWILIO_NUMBER,
                               url='http://7b8659ac.ngrok.io/twiml')
    return Response('phone call placed to ' + outbound_phone_number + '!')


if __name__ == '__main__':
    run(host='127.0.0.1', port=5000, debug=False, reloader=True)