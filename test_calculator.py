from calculator import add, subtract, multiply, divide, CircleArea

def test_add():
	assert add(2,3)==5

def test_divide():
	assert divide(6,2)==3

def test_subtract():
	assert subtract(10,6)==4

def test_multiply():
	assert multiply(3,7)==21

def test_add_uneven():
	a,b=-10,-20
	result=add(a,b)
	assert result==-30

def test_circleArea():
	assert CircleArea(-4) == "NaN"
