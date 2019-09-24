from twilio.rest import Client

class MessageSending():
    def __init__(self, twilio_numer = "+14045864740", number_to_text = "+19259006111"):
        self.twilio_numer = twilio_numer
        self.number_to_text = number_to_text
        self.ACCOUNT_SID = "AC129b5f94d84406f937302d53ab8b01d9"
        self.AUTH_TOKEN = "8d831be37594549d552df18f2b9bc1e6"
        self.client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)
        self.message_body = ""
        


    def send_message(self, time, value, type="tempreture"):
        message_body = "Server Room Alert: {} Tempterature monitor shows that current {} is {}°C. Please check the server room immediately!".format(time, type, value)
        try:
            message = self.client.messages.create(
                to = self.number_to_text,
                from_ = self.twilio_numer,
                body = message_body
            )
            print("Send text Message successfully!")
            print(message_body)
        except:
            print("Fail to send message!")
        


    

    