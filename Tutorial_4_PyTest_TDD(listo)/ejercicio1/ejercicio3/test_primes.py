from primes import is_prime

#si intriducimos 1, entonces no debe ser un numero primo
def test_prime_number():
	assert is_prime(1) == False
def test_prime_number_2():
	assert is_prime(29) == True
def test_prime_number_3():
	assert is_prime(24) == False
