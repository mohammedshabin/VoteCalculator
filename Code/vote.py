import operator

print"---------------------------%_____________________%--------------------------------"

print">>>>>>>>>>>>>>>>>>>>>>>>>>/VOTE COUNTING MACHINE\<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
print"--------------------------------------------------------------------------------"
n = input("ENTER THE NUMBER OF VOTERS IN THE AREA:")
candidates = input("ENTER THE NUMBER OF CANDIDATES:")
CANDIDATES=[]
d = {}
for i in range(candidates):
    print "Enter the name of CANDIDATE No.", i + 1, ":"
    CANDIDATES.append(raw_input())
    d[CANDIDATES[i]] = 0


    
i = 1
while i <= n:
    print "\n\nYOU ARE VOTER NUMBER", i, "\n\n"
    for k in range(candidates):
        print k + 1, ". ", CANDIDATES[k]
    print "YOU VOTE FOR:"

    vote = input()

    if vote <= candidates:
        d[CANDIDATES[vote - 1]] += 1

    else:
        print"THERE IS NO SUCH CANDIDATE YOUR CHANCE IS OVER"
    i = i + 1
print"--------------------------------------------------------------------------------------------------------------------------------------\n"
print"ELECTION RESULTS\n \n"
f = 1


#[k for k,v in dict1.items() if v == 'y']
sorted((d.values()))
print"\n\n"
z = max(d.iteritems(), key=operator.itemgetter(1))[0]
same = -1
for g in d:
    if d[g] == d[z]:
        same += 1
if same < 1:
    print"THE WINNER IS '", z, "'!!!!"
    print"\n\n"
else:
    print"SOME OF THE CANDIDATES HAS GOT SAME NUMBER OF VOTES.ELECTION IS NOT VALID"
    f = 0
w = candidates
for key, value in sorted(d.iteritems(), key=lambda k_v: (k_v[1], k_v[0])):
    print"THE CANDIDATE", key, "AND HAS GOT", value, "NUMBER OF VOTES\n"
    if f == 1:
        print"AND IS AT POSITION", w, "\n\n\n"
        w = w - 1
