from csv import reader
from matplotlib import pyplot
from dateutil import parser

#1 get row ID0 data
with open('Columbus_Ed_astro_pi_datalog.csv', 'r') as f:
    data = list(reader(f))

#2 get row ID 0 data
print(2, data[0])

#3 get row ID 5 data
print(3, data[5])

#4 get last y row ID-1
print(4, data[-1])

#5 get some data temperature
temp = [i[3] for i in data]
print(5, temp)

#6 get some data temperature
temp = [i[3] for i in data[1::]]
print(6, temp)

#7 create a file to store the tempData
temp = []
with open('temp.txt', '') as f:
    for item in temp:
        f.write("%s\n" % item)
        break

#8 another method
f= open('tempData.txt',"w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
	 	f.close() 

#9 get some humidity data

#10 parse time
time = [parser.parse(i[19]) for i in data[1::]]
print(10, time)
      
#11 plot temperature range      
#pyplot.plot(range(len(temp)), temp)
#pyplot.show()

