#!/usr/bin/env python

##############################################
# Elizabeth Brooks - Lab8
#
# Derivative of a Function - Calculates the 
#  derivative of a function. 
##############################################

# Task 1: Accepts a function and float number
#  Returns a function with single float arg
#  When executed, returns 3 element tuple with
#  values of x, value of F(x) at x, and approx
#  derivative at x.
def derive(f, dx):
	def fun(x):
		return (x, f(x), (f(x+dx) - f(x-dx))/(2*dx))
	return fun
		
def main():
	# Define a function to pass in
	def f(x):
		return x*x
	dx = .05
	
	# Testing Task 1
	print "Tests derive. Inputs = x*x, .05, 5 Output = 5, 25, 10"
	print derive(f, dx)(5)

	# Task 2: Same as task 1, but using lambdas
	function = lambda f, dx: lambda x: (x, f(x), (f(x+dx) - f(x-dx))/(2*dx))
	print (function(f, dx)(5))
	
main()