import addOne

print(addOne.addOne(2))

def test_always_passes():
    assert True

#def test_always_fails():
#    assert False

def test_addOne_positive():
    assert addOne.addOne(2)==3
    assert addOne.addOne(0)==1
    assert addOne.addOne(-1)==0

#def test_addOne_negative():
#    assert addOne.addOne(5)==7

def test_minusOne_positive():
    assert addOne.minusOne(2)==1
    assert addOne.minusOne(0)==-1
    assert addOne.minusOne(-10)==-11