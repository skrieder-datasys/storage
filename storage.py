import os
import sys

bucketName = 'skrieder'
# declare the insert
def Insert(key, value):
    try:
        insertCMD = 'gsutil cp '+ sys.argv[2] + ' ' + 'gs://skrieder'
        os.system(insertCMD)
        return True
    except:
        return False

# declare the delete
def Remove(key):
    try:
        removeCMD = 'gsutil rm gs://skrieder/' + sys.argv[2]
        os.system(removeCMD)
        return True
    except:
        return False

#define listing
def Listing(key):
    try:
        #declare bucketname
        bN = key
        #declare constant for gs://
        pre = 6
        # write the output file
        checkCMD = 'gsutil ls gs://skrieder/ > ~/Desktop/storage/output.txt'
        os.system(checkCMD)
        # declare the array
        array2 = []
        ins2 = open( "output.txt", "r" )
        for line2 in ins2:
            line2 = line2[len(bN)+pre:len(line2)-1]
            array2.append(line2)
        #print(array2)
        return(array2)
    except:
        print("Error, exception thrown in Listing()")
        return False

# declare the check
def Check(key):
    try:
        CheckArray = []
        CheckArray = Listing('skrieder')
        KeyToCheck = sys.argv[2]
        if KeyToCheck in CheckArray:
            # print("Key Found!")
            return True
        else:
            # print("Key Not Found!")
            return False
    except:
        return False

# declare the find
def Find(key):
    if Check(key) == True:
        os.system('gsutil cp gs://skrieder/' + key + ' ~/Desktop/storage/')
        #os.system('cat ~/Desktop/storage/'+ key)
        str3 = ""
        ins3 = open( key, "r" )
        for line3 in ins3:
            str3 += line3
        #print(str3)
        return(str3)
    else:
        print("File Not Found!")
        return NULL

# declare the manual
def manual():
    print("Welcome to Python Storage")
    print("The following commands are available:")
    print("Insert:")

###main program###
if(len(sys.argv) > 1):
    if(sys.argv[1] == 'insert'):
        Insert(sys.argv[2], sys.argv[2])
    elif(sys.argv[1] == 'help'):
        manual()
    elif(sys.argv[1] == 'manual'):
        manual()
    elif(sys.argv[1] == 'man'):
        manual()
    elif(sys.argv[1] == 'remove'):
        Remove(sys.argv[2])
    elif(sys.argv[1] == 'check'):
        Check(sys.argv[2])
    elif(sys.argv[1] == 'listing'):
        Listing(sys.argv[2])
    elif(sys.argv[1] == 'find'):
        Find(sys.argv[2])
else:
    print('python storage.py "command"')
    print('type python storage.py help for the manual')

#bucketName = raw_input("Please enter the name of the bucket: ")
#list = 'gsutil ls gs://'

#cmd = list + bucketName
#os.system(cmd)


