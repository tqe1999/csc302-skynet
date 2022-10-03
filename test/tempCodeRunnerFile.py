res = requests.get("http://api:8000")
emoji = emoji_status(res.text == "Hello, world!")
print(f"Hello world: {emoji}")