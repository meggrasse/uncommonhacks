from twilio.rest import TwilioRestClient
from secret import *
 
# Your Account Sid and Auth Token from twilio.com/user/account

client = TwilioRestClient(account_sid, auth_token)
 
call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
    to="+16304702146",
    from_="+16307556548")
print call.sid