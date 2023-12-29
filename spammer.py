import tkinter as tk
import requests
import random

def send_message():
    token1 = token_1.get()
    token2 = token_2.get()
    token3 = token_3.get()
    channel_id = channel.get()
    no = rate.get()
    message = message_entry.get()  
    increase_level = increase_level_var.get()  

    for i in range(int(no)):
        random_number = random.randint(1000000000000000000000000000, 9999999999999999999999999999999999999999)

        if increase_level:
            random_number += i * 1000000000

        url1 = f'https://discord.com/api/v8/channels/{channel_id}/messages'
        data1 = {"content": f"# {message} = {random_number}"}
        headers1 = {"authorization": token1}

        url2 = f'https://discord.com/api/v8/channels/{channel_id}/messages'
        data2 = {"content": f"# {message} = {random_number}"}
        headers2 = {"authorization": token2}

        url3 = f'https://discord.com/api/v8/channels/{channel_id}/messages'
        data3 = {"content": f"# {message} = {random_number}"}
        headers3 = {"authorization": token3}

        requests.post(url1, data=data1, headers=headers1)
        requests.post(url2, data=data2, headers=headers2)
        requests.post(url3, data=data3, headers=headers3)

        loop_count_label.config(text=f"Loops: {i + 1}")

    mission_complete_label.config(text="Mission Complete")

root = tk.Tk()
root.title("Discord Spammer by ZOHAIR AHMED")
root.geometry("400x660")
root.resizable(False, False)

token_1 = tk.Entry(root, width=30, font=("Arial", 12))
token_2 = tk.Entry(root, width=30, font=("Arial", 12))
token_3 = tk.Entry(root, width=30, font=("Arial", 12))
channel = tk.Entry(root, width=30, font=("Arial", 12))
rate = tk.Entry(root, width=30, font=("Arial", 12))
message_entry = tk.Entry(root, width=30, font=("Arial", 12))

labels = [
    ("Token 1", token_1),
    ("Token 2", token_2),
    ("Token 3", token_3),
    ("Channel ID", channel),
    ("No. Of MSG's", rate),
    ("Enter Your Message", message_entry),
]

for text, entry in labels:
    label = tk.Label(root, text=text, font=("Arial", 12))
    label.pack(pady=3)
    entry.pack(pady=10)

increase_level_var = tk.BooleanVar()
increase_level_check = tk.Checkbutton(root, text="Increase Level of random", variable=increase_level_var, font=("Arial", 12))
increase_level_check.pack(pady=10)

loop_count_label = tk.Label(root, text="Loops: 0", font=("Arial", 12))
loop_count_label.pack(pady=10)

mission_complete_label = tk.Label(root, text="", font=("Arial", 14))
mission_complete_label.pack(pady=10)

search_button = tk.Button(root, text="Send Messages", command=send_message)
search_button.pack(pady=10)

github_link_label = tk.Label(root, text="GitHub", font=("Arial", 12), cursor="hand2", fg="blue")
github_link_label.pack(pady=10)

def open_github_link(event):
    import webbrowser
    webbrowser.open("https://github.com/zohair-ahmed-nadeem")

github_link_label.bind("<Button-1>", open_github_link)

# Start the Tkinter event loop
root.mainloop()


