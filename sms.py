import requests
username = 'ACe2197541d369f5ee41a93fb6678bf24d'
password = '876cb6ada35eb4be680375c056ce2d8b'
number_to_text = '+13146498251'
twilio_number = '+13237160239'

message_body= 'Hi there, i am learning!'
def xml_pretty(xml_string):
    import xml.dom.minidom
    xml= xml.dom.minidom.parseString(xml_string)
    pretty_xml_= xml.toprettyxml()
    print(pretty_xml_)
   


base_url = 'https://api.twilio.com/2010-04-01/Accounts'
message_url = base_url + '/'+ username +'/Messages.json'
auth = (username, password)

post_data = {
    "From": twilio_number,
    "To": number_to_text,
    "Body": message_body,
    "MediaUrl": "https://media-cdn.tripadvisor.com/media/photo-s/0e/85/48/e6/seven-mile-beach-grand.jpg"
}

r = requests.post(message_url,data= post_data, auth= auth)

#print(r.status_code)
# xml_pretty(r.text)

message_url_ind = message_url + "/MM7b7eaf09a38646599247bce5db56640c" #"SID";Individual item(ind)
get_r = requests.get(message_url_ind,auth=auth)
xml_pretty(get_r.text)