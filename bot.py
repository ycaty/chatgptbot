from chatgpt_bot import chatgptBot


username = ""
password = ""
gptbot = chatgptBot()

msg = "hello world"

gptbot.doLogin(username,password)

gptbot.send_message(msg)

gptbot.read_all_messages()
input(">>")
