from bank import bankoper
def test_deposit():
    totalbalance , updatebalance = bankoper(200000,30000,0)
    assert totalbalance == 230000
    assert updatebalance == 230000

def test_withdraw():
    totalbalance , updatebalance =bankoper(100000,40000,10000)
    assert totalbalance == 140000
    assert updatebalance == 130000
def test_anyamount():
    totalbalance , updatebalance = bankoper(150000,0,15000)
    assert totalbalance == 150000
    assert updatebalance == 165000
