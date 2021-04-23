from twilio.rest import Client
import os

class PhoneMessenger:

	def __init__(self):

		account_sid = os.getenv('ACCOUNT_SID')
		auth_token = os.getenv('AUTH_TOKEN')

		print(account_sid, auth_token)

		self.client = Client(account_sid, auth_token)

		self.hostNumber = os.getenv('NUMBER')
		self.phoneNumber = os.getenv('MY_NUMBER')


	def sendMessage(self, data):

		message = self.client.messages.create(body=data, from_=[self.hostNumber], to=[self.phoneNumber])
