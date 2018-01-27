import numpy as np
import sys
import csv

if __name__=='__main__':

	caseCount=int(sys.argv[1])
	countInFamily=int(sys.argv[2])
	fileName=sys.argv[3]

	res=np.zeros([caseCount,caseCount])
	resCount=np.zeros([caseCount,caseCount])

	
	with open(fileName) as f:
		curRowNo=0
		reader=csv.reader(f)
		for row in reader:
			rbc=int(curRowNo/countInFamily) #current row belongs to which case
			if rbc>=caseCount:
				break
			del row[0]
			for curColNo in range(0,curRowNo):
				cbc=int(curColNo/countInFamily) #current column belongs to which compare case
				res[rbc,cbc]+=float(row[curColNo])
				resCount[rbc,cbc]+=1
			curRowNo+=1

	sumInFamily=0
	cntInFamily=0
	sumBetFamily=0
	cntBetFamily=0

	with open("res.txt","w+") as f:
		for i in range(caseCount):
			for j in range(i+1):
				res[i,j]/=resCount[i,j]

				if i==j:
					sumInFamily+=res[i,j]
					cntInFamily+=1
				else:
					sumBetFamily+=res[i,j]
					cntBetFamily+=1

				f.write(str(res[i,j]))
				f.write(' ')
			f.write('\n')

	print("the average distance in families is %.2f" % (sumInFamily/cntInFamily))
	print("the average distance between families is %.2f" % (sumBetFamily/cntBetFamily))
	print("the pairwise average distance between families stored in res.txt")



		