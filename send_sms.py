#!/usr/bin/python

from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account

client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="test fam",
    to="+16304702146",    # Replace with your phone number
    from_="+16307556548") # Replace with your Twilio number
print message.sid
