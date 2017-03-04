import csv


def filterThreshold(elem):
    if elem[0] > 58:
        return elem 

def isReckless(elem):
    return True if elem[1] == 1 else False


values = []
with open('dat.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
	if (row[0] != "SPEED"):
            values.append((float(row[0]), int(row[1])))


results = filter(isReckless, filter(filterThreshold, values))

print 
print 
print "-------- RESULTS ----------"
print "Length: " + str(len(results))
print results
print 
print 
