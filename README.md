# agol-webhook-examples
This repo is an example of using a custom ArcGIS Online web hook endpoint using Flask with verification.

It is by no means the best implemenation or most pythonic way of doing it, but hey... it works! 

For whatever reason, webhook data sent from ArcGIS Online needs to be processed as form data as opposed to json. The other issue is that the webhook secret isn't sent in the header, but rather is sent along with the data which can be an issue when creating the computed hash as you have to split it out. The code explains everything a little bit better with the comments.
