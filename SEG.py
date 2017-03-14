from pyspark import SparkConf, SparkContext
import collections, re

#def normalizedWords (text):
#    return re.compile(r'\W+', re.UNICODE).split(text.lower())

def parseLine(line):
    field = line.split(' ')
    return (field)

conf = SparkConf().setMaster("local").setAppName("Word Count")
sc = SparkContext(conf = conf)

input = sc.textFile("file:///Users/Jason/Documents/Simulator/SEGs/12-10-15/3A/APP/V34_Sim_Guides/Integrated_Scenarios/INT01")

word = input.flatMap(parseLine)
wordCount = word.map(lambda x: (x,1)).reduceByKey(lambda x, y: x+y)
sortedResults = wordCount.map(lambda (x,y): (y,x)).sortByKey()

results = sortedResults.collect()

for result in results:
    count = str(result[0])
    word = result[1].encode('ascii', 'ingnore')
    if (word):
        print word + ":\t\t" + count
