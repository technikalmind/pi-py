# Author: George "Technikal Mind" Hall
# Date: 3/15/16
# About: Pi-Calc estimates the value of pi using various infinite series formulas.
from __future__ import division;

def GregoryLeibniz():
	"Uses the Gregory-Leibniz infinite series to calculate Pi"
	
	iter = 1;
	frac = 1;
	pi = 4;
	
	# 1 - 1/3 + 1/5 - 1/7 ...
	for x in range(3, 1000000, 2):		# must begin at 3, increment by 2, and occur an odd number of times
		if(iter % 2):
			pi -= 4/x;	# subtract
		else:
			pi += 4/x;	# add
		iter += 1;
	return pi;

print GregoryLeibniz();
