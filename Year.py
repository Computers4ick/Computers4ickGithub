year = int(input())
if year % 400 == 0:
    print("%d Yes." %year)
elif year % 100 == 0:
    print("%d Ho-ho-ho... No." %year)
elif year % 4 == 0:
    print("%d Yes" %year)
else:
    print("%d Ho-ho-ho... No." %year)
