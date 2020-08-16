a = input('Enter name : ')
b = input('Enter password : ')
print()

if b == 'abc' :
	print('Password correct')
	print('Welcome', a)
	print()
	a = print('a. Addition')
	b = print('b. Subtraction')
	c = print('c. Multiplication')
	d = print('d. Division')
	e = print('e. Multiplication table of number')
	f = print('f. Square table')
	g = print('g. Cube table')
	h = print('h. Square root of number')
	i = print('i. Cube root of number')
	j = print('j. Factors of number')
	k = print('k. Factorial of number')
	l = print('l. Prime number identifier')
	m = print('m. Area and perimeter')
	n = print('n. L.C.M. of two numbers')
	o = print('o. H.C.F. of two numbers')
	print()
	c = input('Choice : ')
	print()
	
	if c == 'a' :
		print('You chose addition')
		s = 0
		a = int(input('Enter number of terms : '))
		for i in range(1, a+1) :
			i = float(input('Enter number : '))
			s += i
		print('Addition : ', s)
		
	elif c == 'b' :
		print('You chose subtraction')
		s1 = float(input('Enter first number : '))
		s2 = float(input('Enter second number : '))
		s3 = s1 - s2
		print('Subtraction : ', s3)
		
	elif c == 'c' :
		print('You chose multiplication')
		m = 1
		a = int(input('Enter number of terms : '))
		for i in range(1, a+1) :
			i = float(input('Enter number : '))
			m *= i
		print('Multiplication : ', m)
		
	elif c == 'd' :
		print('You chose division')
		d1 = float(input('Enter first number : '))
		d2 = float(input('Enter second number : '))
		d3 = d1 / d2
		print('Division : ', d3)
		
	elif c == 'e' :
		print('You chose multiplication table of number')
		t = int(input('Enter number : '))
		for i in range(1, 31) :
			print(t, '×', i, '=', t*i)
			
	elif c == 'f' :
		print('You chose square table')
		for i in range(1, 31) :
			print('Square of', i, '=', i**2)
			
	elif c == 'g' :
		print('You chose cube table')
		for i in range(1, 31) :
			print('Cube of', i, '=', i**3)
			
	elif c == 'h' :
		print('You chose square root of number')
		a = int(input('Enter number : '))
		print('Square root = ', a**(1/2))
		
	elif c == 'i' :
		print('You chose cube root of number')
		a = int(input('Enter number : '))
		print('Cube root = ', a**(1/3))
		
	elif c == 'j' :
		print('You chose factors of number')
		f1 = int(input('Enter number : '))
		print('Factors are :')
		for f2 in range(1, f1+1) :
			f3 = f1 % f2
			if f3 == 0 :
				print(f2)
				
	elif c == 'k' :
		print('You chose factorial of number')
		a = int(input('Enter number : '))
		b = 1
		for i in range(1, a+1) :
			b *= i
		print('Factorial of', a, '=', b)
		
	elif c == 'l' :
		print('You chose prime factor identifier')
		a = int(input('Enter number : '))
		c = 0
		print('Factors are :')
		for b in range(1, a+1) :
			d = a % b
			if d == 0 :
				print(b)
				c += 1
		if c == 2 :
			print('Thus', a, 'is prime number.')
		else :
			print('Thus', a, 'is composite number.')
	
	elif c == 'm' :
		print('You chose area and perimeter')
		a = input('Enter shape : ')
		if a == 'circle' :
			r = float(input('Enter radius : '))
			ar = (22/7) * r**2
			cr = 2 * (22/7) * r
			print('Area : ', ar)
			print('Circumference : ', cr)
		elif a == 'square' :
			l = float(input('Enter length of side : '))
			ar = l**2
			pr = l * 4
			print('Area : ', ar)
			print('Perimeter : ', pr)
		elif a == 'rectangle' :
			l = float(input('Enter length : '))
			b = float(input('Enter breadth : '))
			ar = l * b
			pr = 2 * (l + b)
			print('Area : ', ar)
			print('Perimeter : ', pr)
		else :
			print('Invalid shape')
			
	elif c == 'n' :
		print('You chose L.C.M. of two numbers')
		a = int(input('Enter num1 : '))
		b = int(input('Enter num2 : '))
		if a > b :
			m = a
		else :
			m = b
		while True :
			if m % a == 0 and m % b == 0 :
				print('L.C.M. : ', m)
				break
			m += 1
			
	elif c == 'o' :
		print('You chose H.C.F. of two numbers')
		a = int(input('Enter num1 : '))
		b = int(input('Enter num2 : '))
		if a > b :
			m = b
		else :
			m = a
		while True :
			if a % m == 0 and b % m == 0 :
				print('H.C.F. : ', m)
				break
			m -= 1
			
	else :
		print('Invalid choice')
		
else :
	print('Password incorrect')