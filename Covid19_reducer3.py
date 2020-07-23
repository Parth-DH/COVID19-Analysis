#! /usr/bin/python

from operator import itemgetter 
import sys
from collections import defaultdict


def main():
	cmap = {}
	# popmap = {}
	popmap = defaultdict(int)
	for line in sys.stdin:
		line = line.strip()
		try:
			country, count = line.split(',')
			count = int(count)
			cmap[country] = cmap.get(country, 0) + count
		except:
			region, total_pop = line.split('\t')
			# popmap[region] = int(total_pop)
			popmap[region] += int(total_pop)


	# sort the countrys alphabetically;
	sort_cmap = sorted(cmap.items(), key=itemgetter(0))

	for country, cases in sort_cmap:
		try:
			print ('%s,%s'% (country, (cases*1000000)/popmap[country]))
		except ZeroDivisionError:
			pass
if __name__ == '__main__':
	main()