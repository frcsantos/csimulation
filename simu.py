#!user/bin/python

import sys

def help1():

	print "Provide number of total cells, number of mutated cells, division and death rate (respectively)"


def help2():

	print "Provide number of total cells (int), number of mutated cells (int), division and death rate (floats)"


class cells:
	divrate=dir
	deathrate=der

	def __init__(self,name,mutation):
		self.name=name
		self.mutation=mutation
		cells.count+=1

	def displaycount(self):
		print "There are %d cells in the pool" % cells.count


def setup(startncells, mut, div, death):
	for i in range(1,startncells):
		cellname="C"+str(i)
		varname=str(i)
		if i<=n:
			varname=cells(cellname,1)
		else:
			varname=cells(cellname,0)


def main():

	if sys.argv==[sys.argv[0]]:
		help1()
	elif:
		tc=sys.argv[1]
		mc=sys.argv[2]
		dir=sys.argv[3]
		der=sys.argv[4]
	if type(tc) is not int or type(mc) is not int or type(dir) is not float or type(der) is not float:
		help2()
	else: 
		setup(tc,mc)
	
