sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

if isinstance(sI, int) and sI >= 100:
    print "That's a big number"
else:
    print "That's a small number"

if isinstance(bI, int) and bI >= 100:
    print "That's a big number"
else:
    print "That's a small number"

if isinstance(eI, int) and eI >= 100:
    print "That's a big number"
else:
    print "That's a small number"
if isinstance(spI, int) and spI >= 100:
    print "That's a big number"
else:
    print "That's a small number"

if isinstance(sS, basestring) and len(sS) >= 50:
    print "Long sentence"
else:
    print "Short sentence"
if isinstance(mS, basestring) and len(mS) >= 50:
    print "Long sentence"
else:
    print "Short sentence"
if isinstance(bS, basestring) and len(bS) >= 50:
    print "Long sentence"
else:
    print "Short sentence"
if isinstance(eS, basestring) and len(eS) >= 50:
    print "Long sentence"
else:
    print "Short sentence"

if isinstance(aL, list) and len(aL) >= 10:
    print "Big list"
else:
    print "Short list"
if isinstance(mL, list)  and len(mL) >= 10:
    print "Big list"
else:
    print "Short list"
if isinstance(lL, list) and len(lL) >= 10:
    print "Big list"
else:
    print "Short list"
if isinstance(eL, list) and len(eL) >= 10:
    print "Big list"
else:
    print "Short list"
if isinstance(spL, list) and len(spL) >= 10:
    print "Big list"
else:
    print "Short list"

