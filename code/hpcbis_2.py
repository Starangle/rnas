# whether high performance caused by inner similarity

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

if __name__=='__main__':

	f1=open("res.txt")
	f2=open("rf_list.txt")

	l1s=f1.readlines()
	l2s=f2.readlines()

	f1.close()
	f2.close()

	# 绘制散点图

	x=[]
	y=[]

	scnt=0
	for i in range(0,46):
		socContainer=l2s[i].split()
		s6=float(socContainer[6])
		s7=float(socContainer[7])
		s8=float(socContainer[8])

		dis=float(l1s[i].split()[-1])
		s=max([s6,s7,s8])
		
		s=s8

		if s<0.8:
			scnt+=1
		x.append(dis)
		y.append(s)

	print(scnt)

	# for bound in range(10):

	# 	sumHighSoc=0
	# 	cntHighSoc=0
	# 	sumLowSoc=0
	# 	cntLowSoc=0

	# 	for i in range(0,46):
			
	# 		if y[i]>bound/10:
	# 			sumHighSoc+=x[i]
	# 			cntHighSoc+=1
	# 		else:
	# 			sumLowSoc+=x[i]
	# 			cntLowSoc+=1
	# 	try:
	# 		print("%.2f\t%.2f\t%.2f\t" % (bound/10,sumHighSoc/cntHighSoc,sumLowSoc/cntLowSoc))
	# 	except BaseException:
	# 		print("%.2f\t%.2f\t%.2f\t" % (bound/10,cntHighSoc,cntLowSoc))
			

	# 计算相关系数
	s=[ 0 for i in range(46) ]
	c=[ [] for i in range(46) ]

	for i in range(0,46):
		t=l1s[i].split()
		for j in range(i+1):
			# print("%d %d %d" % (i,j,len(t)))
			if i==j:
				s[i]=float(t[j])
			else:
				c[i].append(float(t[j]))
				c[j].append(float(t[j]))

	for i in range(46):
		c[i]=sum(c[i])/len(c[i]) 
		c[i]/=s[i]

	dc=[]
	dy=[]
	for i in range(46):
		if s[i]>0.8:
			dc.append(c[i])
			dy.append(y[i])

	corr,pvalue=stats.pearsonr(dc,dy)
	print(corr)
	print(pvalue)

	# plt.scatter(x, y)
	# plt.show()
