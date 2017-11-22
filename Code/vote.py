print"---------------------------%_____________________%--------------------------------"

print">>>>>>>>>>>>>>>>>>>>>>>>>>/VOTE COUNTING MACHINE\<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
print"--------------------------------------------------------------------------------"
n=input("ENTER THE NUMBER OF VOTERS IN THE AREA:")
A=0
B=0
C=0
D=0
E=0
a=raw_input("ENTER THE 1st CANDIDATE NAME: ")
b=raw_input("\nENTER THE 2nd CANDIDATE NAME: ")
c=raw_input("\nENTER THE 3rd CANDIDATE NAME: ")
d1=raw_input("\nENTER THE 4th CANDIDATE NAME: ")
e=raw_input("\nENTER THE 5th CANDIDATE NAME: ")
i=1
while i<=n:
 print "\n\nYOU ARE VOTER NUMBER",i,"\n\n"
 print"WHOM DO YOU WISH TO VOTE FOR \n\n1.",a,"  2.",b," 3.",c,"  4.",d1,"  5.",e," :"
 vote=input()
 if vote==1:
  A=A+1
 elif vote==2:
  B=B+1
 elif vote==3:
  C=C+1
 elif vote==4:
  D=D+1
 elif vote==5:
  E=E+1
 else:
  print"THERE IS NO SUCH CANDIDATE YOUR CHANCE IS OVER"
 i=i+1
print"--------------------------------------------------------------------------------------------------------------------------------------\n"
print"ELECTION RESULTS\n \n"
f=1
d={}
d[a]=A
d[b]=B
d[c]=C
d[d1]=D
d[e]=E
sorted((d.values()))
print"\n\n"
if A>B and A>C and A>D and A>E:
 print a,"IS THE ELECTION WINNER\n\n"
elif B>C and B>D and B>E and B>A:
 print b,"IS THE ELECTION WINNER\n\n"
elif C>D and C>E and C>A and C>B:
 print c,"IS THE ELECTION WINNER\n\n"
elif D>E and D>A and D>B and D>C:
 print d,"IS THE ELECTION WINNER\n\n"
elif E>A and E>B and E>C and E>D:
 print e,"IS THE ELECTION WINNER\n\n"
else:
 print"SOME OF THE CANDIDATES HAS GOT SAME NUMBER OF VOTES.ELECTION IS NOT VALID" 
 f=0
w=5
for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k)):
 print"THE CANDIDATE",key,"AND HAS GOT",value,"NUMBER OF VOTES\n"
 if f==1:
  print"AND IS AT POSITION",w,"\n\n\n" 
 w=w-1
