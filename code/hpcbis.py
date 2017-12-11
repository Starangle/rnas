# whether high performance caused by inner similarity

import matplotlib.pyplot as plt

if __name__=='__main__':

	f1=open("res.txt")
	f2=open("rf_list.txt")

	l1s=f1.readlines()
	l2s=f2.readlines()

	f1.close()
	f2.close()

	x=list()
	y=list()

	for i in range(0,46):
		socContainer=l2s[i].split()
		s6=float(socContainer[6])
		s7=float(socContainer[7])
		s8=float(socContainer[8])

		dis=float(l1s[i].split()[-1])
		s=max([s6,s7,s8])

		x.append(dis)
		y.append(s)

	for bound in range(10):

		sumHighSoc=0
		cntHighSoc=0
		sumLowSoc=0
		cntLowSoc=0

		for i in range(0,46):
			
			if y[i]>bound/10:
				sumHighSoc+=x[i]
				cntHighSoc+=1
			else:
				sumLowSoc+=x[i]
				cntLowSoc+=1
		try:
			print("%.2f\t%.2f\t%.2f\t" % (bound/10,sumHighSoc/cntHighSoc,sumLowSoc/cntLowSoc))
		except BaseException:
			print("%.2f\t%.2f\t%.2f\t" % (bound/10,cntHighSoc,cntLowSoc))
			


	plt.scatter(x, y)
	plt.show()
