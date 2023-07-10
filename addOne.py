def addOne(number):
    print("addOne run number:" + str(number))
    return number+1
def main():
    print("main run")

if __name__ == "__main__":
    main()
else:
    print ("main not run. __name__:"+__name__)
