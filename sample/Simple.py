# -*- coding:utf8 -*-
from pyltp import Segmentor

class pnn_count():
	def __init__(self):
		self.mydict = {}
		self.segmentor = Segmentor()
		self.segmentor.load('cws.model')
		self.hash_dict()
		self.ltp_process()
	def ltp_process(self):
		sentence_num = 0
		right_num = 0;
		f = open('pnn_annotated.txt','r')
		for line in f:
			sentence_num += 1
			#print line
			line_array = line.split('\t')
			line = line_array[1]
			count = 0
			words = self.segmentor.segment(line)
			for i in words:
				if self.mydict.has_key(i):
					count = count + self.mydict[i]
			if count > 0:		
				answer = "positive"
				if line_array[0] == '1':
					right_num += 1
			elif count == 0:
				answer = "neuter"
				if line_array[0] == '0':
					right_num += 1
			else:
				answer = "negative"
				if line_array[0] == '-1':
					right_num += 1
			#print "My guess is %s" %answer
			#print "THe right answer is %s" %line_array[0]

			#print "result  %d" % count
		f.close()
		print "total sentence is %d, right answer is %d" %(sentence_num,right_num)
	def hash_dict(self):
		f = open('negative.txt','r')
		for line in f:
			line = line.strip('\n')
			line = line.strip('\r')
			self.mydict[line] = -1
		f.close()
		f = open('positive.txt','r')
		for line in f:
			line = line.strip('\n')
			line = line.strip('\r')
			self.mydict[line] = 1
		f.close()


pnn_count()
