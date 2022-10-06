import requests


def emoji_status(status):
    if status:
        return "✅"
    return "❌"


def hello_world_test():
    try:
        res = requests.get("http://api:8000")
        emoji = emoji_status(res.text == "Hello, world!")
    except:
        emoji = emoji_status(False)
    finally:
        print(f"Hello world: {emoji}")


def failing_host_test():
    try:
        res = requests.get("http://localhost:8000")
        emoji = emoji_status(res)
    except:
        emoji = emoji_status(False)
    finally:
        print(f"Wrong host (failing): {emoji}")


print("running tests...")
hello_world_test()
failing_host_test()
print("tests done")
