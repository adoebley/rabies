#THIS IS WRITTEN IN PYTHON2
#to run it from the command line: 
# $ python2 date_format.py path/input_fasta_filename.fasta path/output_fasta_filename.fasta

import sys
with open(str(sys.argv[1]),'r') as fasta:
	fasta_data = fasta.readlines()
countup,no_date,full_date,year_and_month,year_only,errors=0,0,0,0,0,0

output=[]
for n in range(0,len(fasta_data)):
	if fasta_data[n][0]=='>':
		countup=countup+1
		fasta_data[n]=fasta_data[n].split('|')
		if fasta_data[n][3]=='NA':
			fasta_data[n][3]='XXXX-XX-XX'
			no_date=no_date+1
		elif len(fasta_data[n][3].split('_'))==3:
			fasta_data[n][3]='-'.join(fasta_data[n][3].split('_'))
			full_date=full_date+1
		elif len(fasta_data[n][3].split('_'))==2 and len(fasta_data[n][3])==7:
			fasta_data[n][3]='-'.join(fasta_data[n][3].split('_'))+'-XX'
			year_and_month=year_and_month+1
		elif len(fasta_data[n][3])==4 and fasta_data[n][3].isdigit():
			fasta_data[n][3]=fasta_data[n][3]+'-XX-XX'
			year_only=year_only+1
		else:
			errors=errors+1
		fasta_data[n]='|'.join(fasta_data[n])
		output.append(fasta_data[n])
			
	else:
		output.append(fasta_data[n])
	
#print fasta_data[0]
print 'total_sequences: '+str(countup)
print 'missing_date: '+str(no_date)
print 'complete_date: '+str(full_date)
print 'year_and_month_only: '+str(year_and_month)
print 'year_only: '+str(year_only)
print 'total_dates_corrected: '+str(no_date+full_date+year_and_month+year_only)
print 'not_corrected: '+str(errors)

with open(str(sys.argv[2]),'w+') as f:
	for line in output:
		f.write(str(line))