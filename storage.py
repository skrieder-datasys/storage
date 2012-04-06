import os
import sys

bucketName = 'skrieder'
# declare the insert
def insert(key, value):
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

# declare the check
def Check(key):
    try:
        checkCMD = 'gsutil ls gs://skrieder/ > ~/Desktop/storage/output.txt'
        os.system(checkCMD)
        ReadFilee = '~/Desktop/storage/output.txt'
        ins = open( ReadFile, "r" )
        array = []
        print("in check")
        for line in ins:
            array.append( line )
        print(array)
        return True
    except:
        return False

# declare the manual
def manual():
    print("Welcome to Python Storage")
    print("The following commands are available:")
    print("Insert:")

###main program###
if(len(sys.argv) > 1):
    if(sys.argv[1] == 'insert'):
        insert(sys.argv[2], sys.argv[2])
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
else:
    print('python storage.py "command"')
    print('type python storage.py help for the manual')

#bucketName = raw_input("Please enter the name of the bucket: ")
#list = 'gsutil ls gs://'

#cmd = list + bucketName
#os.system(cmd)


