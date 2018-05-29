import sys
import time

f = open(sys.argv[1], "r")

allLines = f.readlines()
nodeCount = {}
nodeVal = {}
nodeInVals = {}
d = .85

start = time.clock()

for line in allLines:
	line = line.split(",")
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

fin = time.clock() - start
totalLen = len(nodeCount)

for node in nodeCount.keys():
	nodeVal[node] = 1/totalLen

start = time.clock()
epsilon = 9999
iterations = 0
while epsilon >= (1/totalLen)/1000:
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
	epsilon /= totalLen

answer = nodeVal.items()
answer = sorted(answer, key=lambda tup: tup[1], reverse = True)

i = 1
for thing in answer:
	print(i," ",thing[0]," with pagerank ",thing[1])
	i += 1

new = time.clock() - start
print("Read time is: ", fin)
print("Process time is: ",new)
print(i," iterations")

