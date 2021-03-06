# -*- coding: utf-8 -*-
import sys
import os
import math

##################################################################################################
### Capturing the input from the parameters
##################################################################################################

metrics_file = sys.argv[1]
outputfile = sys.argv[2]

##################################################################################################
### Performing the calculation
##################################################################################################

#Get the recommender list
fin = open(metrics_file, "r")
metrics = []
for i in fin:
	i = i.rstrip()
	values = i.split(" ")
	values = [float(i) for i in values]
	metrics += [values]
fin.close()

#calculating the mean
avg = [0 for i in range(len(metrics[0]))]
for i in range(len(metrics)):
	for j in range(len(metrics[i])):
		avg[j] += metrics[i][j]
for j in range(len(avg)):
	avg[j] /= float(len(metrics))

##################################################################################################
### Printing the results in the file and ploting the results
##################################################################################################

#printing results
f = open(outputfile, "w")
for j in range(0, len(avg)):
	f.write("Metric"+str(j+1)+"\t"+str(avg[j])+"\n")
f.close()

#calling the plot
os.system("gnuplot -e \"datafile='"+outputfile+"'; outputname='"+outputfile[:-4]+".png"+"'; maxy='"+str(max(avg)+0.05)+"'\" gnuplot_mean.gp")