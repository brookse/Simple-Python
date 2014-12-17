#!/usr/bin/env python

##############################################
# Elizabeth Brooks - Lab7
#
# Letter Frequency Counting - Takes a string 
#   and builds a frequency listing of 
#   characters found in it. Frequency listing
#   is represented as a dictionary.
#   Returns a dictionary with letters as keys
#   and values as as frequency of letter. Only
#   includes letters with non-zero frequency.
##############################################

def char_freq(string):
	dic = dict()
	# iterate through each character
	for c in string:	
		# see if already in dictionary
		if c in dic:	
			# if yes, increment value to appropriate key
			dic[c] = dic[c] + 1	
		else:	
			# if no, add to dictionary with value of 1
			dic[c] = 1
	
	return dic
	
def main():
	print "test 1, input (hello) output h:1, e:1, l:2, o:1"
	print char_freq("hello")
	print "test 2, input (AAAaaaghgh) output A:3, a:3, g:2, h:2"
	print char_freq("AAAaaaghgh")
	print "test 1, input (i am me) output i:1, ' ':2, a:1, m:2, e:1" 
	print char_freq("i am me")
	
main()