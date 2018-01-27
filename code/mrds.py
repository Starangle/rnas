# make random data set
import os
import random

if __name__=='__main__':
	curDir=os.getcwd()	#获取当前路径

	writer=open('rf_collect.fasta',"w+")

	for fileName in os.listdir(curDir):
		if os.path.splitext(fileName)[1]=='.fa':
			f=open(fileName)
			text=f.readlines()
			idxs=range(1,int(len(text)/2))
			sidxs=random.sample(idxs,10)
			
			seqs=list()
			for i in sidxs:
				j=i*2
				seqs.append(text[j-2])
				seqs.append(text[j-1])

			writer.writelines(seqs)
			f.close()
	writer.close()