try:
    f = open('simple.txt', 'w')
    f.write("Test write to simple text!")
except IOError:
    print("ERROR: Could not find or read data")
else:
    print("SUCCESS")
    f.close()
finally:
    print("I always work no matter what")

