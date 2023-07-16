import addOne

print(addOne.addOne(2))

def test_always_passes():
    assert True

def test_always_fails():
    assert False

def test_addOne_positive():
    assert addOne.addOne(2)==3

def test_addOne_negative():
    assert addOne.addOne(5)==7