# Author: George "Technikal Mind" Hall
# Date: 3/15/16
# About: Pi-Calc estimates the value of pi using various infinite series formulas.
from __future__ import division;

# Begin GregoryLeibniz
# Note: With this method, pi is accurate to 3.14159 after ~450,000 iterations
def GregoryLeibniz():
	"Uses the Gregory-Leibniz infinite series to calculate Pi"
	
	iter = 0;
	pi = 4;
	
	# 1 - 1/3 + 1/5 - 1/7 ...
	for x in range(3, 900002, 2):	# must begin at 3, increment by 2, and occur an odd number of times
		if(not iter % 2):			# only subtract on odd steps (1st iteration should subtract, 2nd add, 3rd sub)
			pi -= 4/x;
		else:
			pi += 4/x;
		iter += 1;
	return str(pi) + " after " + str(iter) + " iterations";
# End GregoryLeibniz

# Begin Nilakantha
# Note: With this method, pi is accurate to 3.14159 after ~45 iterations
def Nilakantha():
	"Uses the Nilakantha infinite series to calculate Pi"
	
	iter = 0;
	pi = 3;
	frac = 0;
	
	for x in range(2, 91, 2):
		y = x+1;
		z = x+2;
		
		if(not iter % 2):
			pi += 4/(x*y*z);
		else:
			pi -= 4/(x*y*z);
		iter += 1;
	return str(pi) + " after " + str(iter) + " iterations";
# End Nilakantha

print GregoryLeibniz();
print Nilakantha();

