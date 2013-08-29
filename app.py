from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
from twilio import twiml
from twilio.util import TwilioCapability
from twilio.rest import TwilioRestClient
import os
from random import choice
from local_settings import *

# SONYA_APP_SID
# BSS_SPAM_ID

# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config['ACCOUNT_SID'] = ACCOUNT_SID
app.config['AUTH_TOKEN'] = AUTH_TOKEN
app.config['BSSSPAM_APP_SID'] = BSSSPAM_APP_SID
app.config['BSS_SPAM_ID'] = BSS_SPAM_ID


@app.route('/')
def index():
    reason = quotes()
    capability = TwilioCapability(app.config['ACCOUNT_SID'],
        app.config['AUTH_TOKEN'])
    capability.allow_client_outgoing(app.config['BSSSPAM_APP_SID'])
    token = capability.generate()
    return render_template('index.html', token=token, reason=reason)


@app.route('/sms', methods=['POST'])
def sms():
    r = twiml.Response()
    reason = quotes()
    r.sms(reason)
    return str(r)


def quotes():
    reasons = [
            'Comic of the day: xkcd.com/149',
            'Comic of the day: xkcd.com/244',
            'Comic of the day: xkcd.com/616',
            'Comic of the day: http://theoatmeal.com/comics/dog_how_see',
            'Comic of the day: http://theoatmeal.com/comics/tesla',
            'Comic of the day: http://theoatmeal.com/comics/wwddd',
            'Comic of the day: http://xkcd.com/181/',]
    return choice(reasons)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
