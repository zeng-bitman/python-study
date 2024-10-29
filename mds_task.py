mds_task = [23, 'Jane', (560), ['Lesson', 'Maths', {'currency' : 'KES'}], 987, (76,'John')]

#print KES
print(mds_task[3][2]["currency"])

#print 500
print(mds_task[2])

#print maths
print(mds_task[3][1])

#add another key ammount with value 90

mds_task[3][2]['ammount'] = 90
print(mds_task)

#reverse 987 to 789 with inbuilt method or assigning manuallly
#*find the index 987
#*convert yo string
#*reverse the sring
#*convert to interger
#*print the output
mds_task[4]=str(mds_task[4])
mds_task[4]=mds_task[4][::-1]
mds_task[4]=int(mds_task[4])
print(mds_task)

#change john to jane
mds_task[5]=()