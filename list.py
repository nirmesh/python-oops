subjects=['physics','math']
games=['chess','cricket']
#print(subjects*2 +games);

#print(subjects[0:5])# doesn't matter if u are asking more

# tuples are immutable u can't append etc

# football=('a','b','c')
# cricket=('x','y','z');
#
#
# print(football[1]);
# print(football.index('c'))
#
# print(football[0:2])
# print(football.count('a'))
#
#
# players=[('a','b','c'),('x','y','z')]
# print(players[1][2]);
#


str="hello nirmesh"
print(str.__len__());

print(str.index('n'))

print(str[::-1]) # reverse ur string

if "n" in str:
    print("element  present")

#it is case sensitive so wont print anything
if "N" in str:
    print("element  not present")

#another way  is not in

if "N" not in str:
    print("capital N not present")