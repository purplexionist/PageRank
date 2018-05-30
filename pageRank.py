#py pageRank.py <file in our directory>
#for les-mis, only finding who occurs with most people. ignoring the extra numbers

import sys
import time

f = open(sys.argv[1], "r")

if sys.argv[1] != "soc-LiveJournal1.txt":
	allLines = f.readlines()
nodeCount = {}
nodeVal = {}
nodeInVals = {}
d = .85

start = time.clock()
if(sys.argv[1] == "stateborders.csv" or sys.argv[1] == "karate.csv" or sys.argv[1] == "dolphins.csv" or sys.argv[1] == "lesmis.csv"):
	for line in allLines:
		line = line.replace("\n", "").split(",")
		if line[2] == "\"NB\"":
			line[2] = "\"NE\""
		if line[2] == "\"MV\"":
			line[2] = "\"WV\""
		if line[2] not in nodeCount:
			nodeCount[line[2]] = 1
		else:
			nodeCount[line[2]] += 1
		if line[0] not in nodeInVals:
			tempList = []
			tempList.append(line[2])
			nodeInVals[line[0]] = tempList
		else:
			nodeInVals[line[0]].append(line[2])
elif sys.argv[1] == "NCAA_football.csv":
	for line in allLines:
		line = line.replace("\n", "").split(",")
		first = line[0].strip()
		second = line[2].strip()
		if first not in nodeCount:
			nodeCount[first] = 0
		if second not in nodeCount:
			nodeCount[second] = 1
		else:
			nodeCount[second] += 1
		if second not in nodeInVals:
			tempList = []
			nodeInVals[second] = tempList
		if first not in nodeInVals:
			tempList = []
			tempList.append(second)
			nodeInVals[first] = tempList
		else:
			nodeInVals[first].append(second)
elif sys.argv[1] == "wiki-Vote.txt" or sys.argv[1] == "p2p-Gnutella05.txt" or sys.argv[1] == "soc-sign-Slashdot081106.txt" or sys.argv[1] == "amazon0505.txt":
	allLines = allLines[4:]
	for line in allLines:
		line = line.split()
		first = line[0]
		second = line[1]
		if second not in nodeCount:
			nodeCount[second] = 0
		if first not in nodeCount:
			nodeCount[first] = 1
		else:
			nodeCount[first] += 1
		if first not in nodeInVals:
			tempList = []
			nodeInVals[first] = tempList
		if second not in nodeInVals:
			tempList = []
			tempList.append(first)
			nodeInVals[second] = tempList
		else:
			nodeInVals[second].append(first)
elif sys.argv[1] == "soc-LiveJournal1.txt":
	for line in f:
		if line[0] != "#":
			line = line.split()
			first = int(line[0])
			second = int(line[1])
			if second not in nodeCount:
				nodeCount[second] = 0
			if first not in nodeCount:
				nodeCount[first] = 1
			else:
				nodeCount[first] += 1
			if first not in nodeInVals:
				tempList = []
				nodeInVals[first] = tempList
			if second not in nodeInVals:
				tempList = []
				tempList.append(first)
				nodeInVals[second] = tempList
			else:
				nodeInVals[second].append(first)

f.close()
fin = time.clock() - start
totalLen = len(nodeCount)

for node in nodeCount.keys():
	nodeVal[node] = 1/totalLen

start = time.clock()
epsilon = 9999
iterations = 0
while epsilon >= (1/totalLen):
	iterations += 1
	epsilon = 0
	tempDict = {}
	for node in nodeVal.keys():
		total = (1-d)/totalLen
		for InNode in nodeInVals[node]:
			total += d*nodeVal[InNode] / nodeCount[InNode]
		epsilon += abs(nodeVal[node] - total)
		tempDict[node] = total
	nodeVal = tempDict
	tempDict = None

answer = nodeVal.items()
answer = sorted(answer, key=lambda tup: tup[1], reverse = True)

i = 1
answerLen = len(answer)
iterCount = min(answerLen, 50)
for j in range(0, iterCount):
	print(i," ",answer[j][0]," with pagerank ",answer[j][1])
	i += 1


new = time.clock() - start
print("Read time is: ", fin)
print("Process time is: ",new)
print(iterations," iterations")

