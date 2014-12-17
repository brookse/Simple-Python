#!/usr/bin/env python

##############################################
# Elizabeth Brooks - Lab7
#
# Filtering Words - Takes in a string of words
#   separated by spaces and an integer (n); 
#   returns string containing only words 
#   longer than that integer. Words stay in 
#   the same order as original string.
##############################################

def filter_long_words(string, n):
	# split string by spaces
	words = string.split()
	retVal = "";
	# iterate through all words
	for i in words:
		# check each word is more than n
		if len(i) > n:
			# if so, add to new string
			retVal = retVal + i + " "
	
	return retVal
	
def main():
	print "test 1, input (Hello my name is Computer, 4) output (Hello Computer)"
	print filter_long_words(string="Hello my name is Computer", n=4)
	print "test 2, input (my  sentence is cool, 2) output (sentence cool)"
	print filter_long_words(string="my  sentence is cool", n=2)
	
main()