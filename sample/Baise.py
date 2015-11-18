# -*- coding:utf8 -*-

from pyltp import Segmentor
class pnn_count():
	def __init__(self):
		self.mydict = {}
		self.lines = []
		self.lines_num = 3000
		self.c = [0,0,0] #PNN
		self.w_c = [{},{},{}]
		self.segmentor = Segmentor()
		self.segmentor.load('cws.model')
		self.read_file()
		self.train()
		self.test()
	def read_file(self):
		f = open('pnn_annotated.txt','r')
		self.lines = f.readlines()
		f.close()
	def train(self):
		for i in range(0,self.lines_num/5*4):
			line = self.lines[i]
			line.strip('\n')
			line_array = line.split('\t')
			line = line_array[1]
			words = self.segmentor.segment(line)
			if line_array[0] == '1':
				pos = 0
			elif line_array[0] =='0':
				pos = 1
			else:
				pos = 2
			for i in words:                          #calculate frequency
				if self.w_c[pos].has_key(i):
					self.w_c[pos][i] += 1
				else:
					for a in range(0,3):
						self.w_c[a][i] = 0
					self.w_c[pos][i] += 1
			self.c[pos] += 1

	def test(self):
		count = 0
		v = len(self.mydict.keys())
		for a in range(self.lines_num / 5 * 4, len(self.lines)-1):
			wholeline = self.lines[a]
			print wholeline
			result = [0.0,0.0,0.0]
			line_array = wholeline.split('\t')
			line = line_array[1]
			words = self.segmentor.segment(line)
			for i in range(0,3):
				pci = 1.0 * self.c[i] / (self.lines_num/5 *4)
				pwci = 1.0
				sum_i = 0
				for q in self.w_c[i].keys():
					sum_i += self.w_c[i][q]
				for k in words:
					if self.w_c[i].has_key(k):
						pwci = pwci * (self.w_c[i][k] + 1) / (sum_i + v)
				result[i] = pci * pwci
			maxi = 0
			for i in range(0,3):
				if result[i]>result[maxi]:
					maxi = i
			if maxi ==0:
				if line_array[0] == '1':
					count += 1
				print "my guess is positive"
			elif maxi==1:
				if line_array[0] == '0':
					count += 1
				print "my guess is neuter"
			else:
				if line_array[0] == '-1':
					count += 1
				print "my guess is negative"
		print  count * 1.0 /(self.lines_num/5)
pnn_count()
