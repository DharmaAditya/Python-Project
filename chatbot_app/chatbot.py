import google.generativeai as genai

API_Key = "AIzaSyB76DbP3no2KYWj6-wlxJHOt1v3UFc3Pd0"
genai.configure(api_key=API_Key)

model = genai.GenerativeModel("gemini-2.0-flash")

chat = model.start_chat()

print("Chat with Genimi! Type exit to quit")
print('-' * 50)

response = chat.send_message("Hello")
print("Gemini:", response.text)
while True:
    user_input = input("You:")
    if user_input.lower() == "exit":
        break
    response = chat.send_message(user_input)
    print("Gemini:", response.text)