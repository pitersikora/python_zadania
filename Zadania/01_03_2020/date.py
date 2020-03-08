# Date.py

rok1 = '2002'
miesiac1 = '12'
dzien1 = '15'

rok2 = '2004'
miesiac2 = '12'
dzien2 = '15'

string1 = rok1 + miesiac1 + dzien1
string2 = rok2 + miesiac2 + dzien2

for i in range(0, len(string1)):
    if string1[i] < string2[i]:
        print "Data %s_%s_%s wydarzyla sie wczesniej" % (rok1, miesiac1, dzien1)
        exit(0)
    if string1[i] > string2[i]:
        print "Data %s_%s_%s wydarzyla sie wczesniej" % (rok2, miesiac2, dzien2)
        exit(0)

print "obie daty sa jednakowe"