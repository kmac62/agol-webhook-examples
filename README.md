# agol-webhook-examples
This repo is an example of using a custom ArcGIS Online web hook endpoint using Flask with verification.

It is by no means the best implemenation or most pythonic way of doing it, but hey... it works! 

Here is why things are goofy when dealing with web hooks sent from ArcGIS Online:

The signature hash is computed normally on AGOL's end with the payload and secret using sha256. However, in the payload of the webhook is a url that is used to run the extract changes job via the REST API. The issue is that this url gets parsed when you call Flask's request.form method but the hash was generated on AGOL's end with the url encoded. To get the encoded url, you have to call Flask's get_data() method which will include the encoded url for the extract changes job. I've tried using urllib to encode the url which would eliminate the need to use regex to split the data but it wouldn't return the correct hash for whatever reason... probably an issue with my coding ability more than anything. 
