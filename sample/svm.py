# coding: utf-8
#
from tgrocery import Grocery

LINES_NUM = 3000
FOLDS_NUM = 5
grocery = Grocery('test')
f = open("pnn_annotated.txt",'r')
lines = []	
lines = f.readlines()

f.close()
def train_test(test_whichpart):

	count = 0
	train_sentences = []
	test_sentences = []
	for i in lines:
		count += 1
		i.strip('\n')
		line_array = []
		line_array = i.split('\t')
		if((count>LINES_NUM * 1.0/ FOLDS_NUM * (test_whichpart -1)) and (count <LINES_NUM * 1.0/FOLDS_NUM * test_whichpart)):
			test_sentences.append([line_array[0],line_array[1]])
		else:
			train_sentences.append((line_array[0],line_array[1]))
	grocery.train(train_sentences)
	print grocery.get_load_status()

	rightans = 0
	for k in test_sentences:
		predict_result = grocery.predict(k[1])
		print k[0] + " 	 " + k[1]
		print "My answer is : %s " %predict_result
		print ""
		print '########################################'
		if predict_result == k[0]:
			rightans += 1
	print "the accuracy rate is ; %f" %(rightans *1.0 /LINES_NUM * 5)
	

train_test(1)
train_test(2)
train_test(3)
train_test(4)
train_test(5)

#print predict_result.dec_values

# grocery = Grocery('read_text')
# train_src = '../text_src/train_ch.txt'
# grocery.train(train_src)
# print grocery.get_load_status()
# predict_result = grocery.predict('考生必读：新托福写作考试评分标准')
# print predict_result
# print predict_result.dec_values