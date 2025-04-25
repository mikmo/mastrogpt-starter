import sys 
sys.path.append("packages/pcarucci/chat")
import chat

def test_chat():
    res = chat.chat({})
    assert res["output"] == "chat"
