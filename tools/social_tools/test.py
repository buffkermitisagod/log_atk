user = "test"

run_til = 0

print("reading...")

name = "face/"+user+".txt"

try:
    f = open(name,"r")
    num = f.readline()[0]
    f.close()
    run_til = int(num)
except FileNotFoundError:
    f = open(name,"x")
    f.close()