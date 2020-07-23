#! /usr/bin/python

from operator import itemgetter 
import sys

cmap = {}

def main():
	for line in sys.stdin:
		line = line.strip()
		country, count = line.split(',')
		try:
			count = int(count)
			cmap[country] = cmap.get(country, 0) + count
		except ValueError:
			pass

	# sort the countrys alphabetically;
	sort_cmap = sorted(cmap.items(), key=itemgetter(0))

	for country, cases in sort_cmap:
		print ('%s,%s'% (country, cases))

if __name__ == '__main__':
	main()