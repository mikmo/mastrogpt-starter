import sys 
sys.path.append("packages/pcarucci/reverse")
import reverse

def test_reverse():
    args = { "input": "ciao"}
    res = reverse.reverse(args)
    assert res["output"] == "oaic"
