# whether high performance caused by inner similarity
import matplotlib.pyplot as plt

if __name__=='__main__':

	f1=open("res.txt")
	f2=open("rf_list.txt")

	l1s=f1.readlines()
	l2s=f2.readlines()

	f1.close()
	f2.close()

	sumHighSoc=0
	cntHighSoc=0
	sumLowSoc=0
	cntLowSoc=0

	bound=0.85

	x=list()
	y=list()

	for i in range(0,46):
		socContainer=l2s[i].split()
		s6=float(socContainer[6])
		s7=float(socContainer[7])
		s8=float(socContainer[8])

		dis=float(l1s[i].split()[-1])
		if s6>bound or s7>bound or s8>bound:
			sumHighSoc+=dis
			cntHighSoc+=1
		else:
			sumLowSoc+=dis
			cntLowSoc+=1

		x.append(dis)
		y.append(s8)

	print("the average distance in high socre families is %f" % (sumHighSoc/cntHighSoc))
	print("the average distance in low socre families is %f" % (sumLowSoc/cntLowSoc))

	plt.scatter(x, y)
	plt.show()
