from subprocess import Popen, PIPE
import numpy
import os
# ML: Length of teh Motif
# X: Major Factor of Clustor Radius
# K: Minor Factor of Clustor Radius
# Refer to http://www.cs.ucr.edu/~eamonn/exact_motif/
# This Programm is a modified version of Exact Discovery of Time Series Motifs, by Abdullah Mueen, Eamonn Keogh, Qiang Zhu, Sydney Cash and Brandon Westover.
# Instead of using Number of motifs, a new factor has been replaced, called Major factor of cluster radius. This factor multplies the first non- zero bsf(best-so-far) 
# 		to drive bsfb(best-so-far-break). Minor factor of cluster radius then gets used to determine, other motifs after finding the first two.
def MotifDetect(Data,ML,X,K):
	try:
		if type(Data)==list:
			Data=numpy.asarray(Data)
		else:
			if type(Data) is not numpy.ndarray: 
				raise ValueError
	except ValueError: 
		print("Input data should be list or numpy array type.")
	try:
		if len(Data.shape)==1:
			Len=Data.shape[0]
		else:
			raise ValueError
	except ValueError: 
		print("Input data should be 1-Dimensional.")
	# str(Len) ,str(ML),str(X),str(K),"50"
	#  Length of Time Series, determined automatically based on input signal.
	# "50": Number of reference points refer to Mueen paper for more info.
	numpy.savetxt("tmp.txt", Data, fmt='%.18e', delimiter=' ', newline='\n')
	cmd=["MD.exe", "tmp.txt", str(Len) ,str(ML),str(X),str(K),"10"]
	p = Popen(cmd, stdout=PIPE, universal_newlines=True)
	stdout_text = p.communicate(input="1\n\n")[0]
	os.remove("tmp.txt")
	values=[st1 for st1 in stdout_text.split(";")]
	points=[[int(i) for i in st2.split(",")] for st2 in values[:-1]]
	Output=[]
	for i in points:
		out=[]
		for j in i:
			out.append(Data[j:j+ML])
		Output.append(out)
#   Return is a list of numpy arrays, best-so-far-break
	return Output,values[-1]


