import requests
from twilio.rest import Client

username = 'ACe2197541d369f5ee41a93fb6678bf24d'
password = '876cb6ada35eb4be680375c056ce2d8b'

client = Client(username, password)

number_to_text = '+13146498251'
twilio_number = '+13237160239'
message_body= 'Another new one!!'
media_url = 'https://media-cdn.tripadvisor.com/media/photo-s/0e/85/48/e6/seven-mile-beach-grand.jpg'

"""
Create / Send POST METHOD
"""
message = client.messages.create(
    to = number_to_text,
    from_ = twilio_number,
    body=message_body,
    media_url=media_url
)
print(message.sid)
#print(message.media_list.list())

def xml_pretty(xml_string):
    import xml.dom.minidom
    xml= xml.dom.minidom.parseString(xml_string)
    pretty_xml_= xml.toprettyxml()
    print(pretty_xml_)