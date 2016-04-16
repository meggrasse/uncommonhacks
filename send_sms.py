#!/usr/bin/python

from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC01fe30b094e3251e3f48f0acb4853310"
auth_token  = "47c5f4501af1693a8ecfdcd887aa2632"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="test fam",
    to="+16304702146",    # Replace with your phone number
    from_="+16307556548") # Replace with your Twilio number
print message.sid
