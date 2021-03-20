import json, hmac, base64, os, re
from flask import Flask, request, abort
from hashlib import sha256


webhook = Flask(__name__)


@webhook.route('/', methods=['POST'])
def webhook():
    if request.method == 'POST':
        verification = verify_hook(request.get_data(), request.form)
        if verification:
            #do stuff
            return '', 200
        else:
            abort(403)
    else:
        abort(403)


def verify_hook(data, form):
    payload = re.split(b'payload=|&', data)[1] # splits the bytes data to separate the data from the signature. 
    secret = os.getenv('foo').encode('utf-8') # gets your password/secret from the environment variables.
    signature = 'sha256=' + base64.b64encode(hmac.new(secret, payload, digestmod=sha256).digest()).decode() # this is really sloppy, but it works for now. 
    return hmac.compare_digest(signature, form['x-esriHook-Signature'])
  
