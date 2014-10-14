print "how many numbers do you want to add"
total = raw_input() 

maxtotal = 0
for x in range(int(total)):
    print "what number do you want to add together?"
    userInput = int(raw_input())
    maxtotal = int(maxtotal) + int(userInput)

print maxtotal



print "how many numbers do you want to add"
total = raw_input() 

maxtotal = []
for x in range(int(total)):
    print "what number do you want to add together?"
    userInput = int(raw_input())
    maxtotal.append(userInput)

print maxtotal
print sum(maxtotal)



print "what number do you want the factorial from?"
total = int(raw_input())

maxtotal = total
for x in range(2,total):
    maxtotal *= x
print maxtotal 


print "how many numbers do you want the factor's from "
total = int(raw_input()) 

maxtotal = []
for x in range(1,total):
    if (total % x) == 0:
        maxtotal.append(x)    
maxtotal.append(total)
print maxtotal

