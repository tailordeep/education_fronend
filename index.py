import pywhatkit

# Replace 'phone_number' with the desired phone number (in international format)
phone_number = "+917046135194"

# Replace 'message' with your message content
message = "Hello from Python!"

# Send the message
pywhatkit.sendwhatmsg(phone_number, message, 12, 0)