import re
from ftplib import FTP

if __name__=='__main__':

	suffix='.fa.gz'
	ftp=FTP("ftp.ebi.ac.uk")
	ftp.login()
	ftp.cwd("pub/databases/Rfam/CURRENT/fasta_files")
	
	fRfList=open("rf_list.txt")
	for line in fRfList.readlines():
		name=line.split()[1]
		
		fileName=name+suffix
		cmd="RETR "+fileName
		ftp.retrbinary(cmd,open(fileName,'wb').write)

	ftp.quit()