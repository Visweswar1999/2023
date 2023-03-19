import pytest

@pytest.fixture()
def testmain():
    print("hello")

def testfirst(testmain):
    print("This is the first method")

def testsecond(testmain):
    print("inside the second fixture method")

@pytest.yield_fixture()
def testyieldone():
    print("inside the yield one")

def testfixy(testyieldone):
    print("inside the second yield")

def testfix2(testyieldone):
    print("front and back")



