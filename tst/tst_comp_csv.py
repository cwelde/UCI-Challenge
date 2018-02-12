import pandas as pd

#compares two csv files and determines if they are the same or not

def compareFiles(file1, file2):

   df1 = pd.read_csv(file1)
   df2 = pd.read_csv(file2)

   if df1.equals(df2):
       return 0
   else:
       return 1


#getFile1 = input('Enter the name of the first file: ')
#getFile2 = input('Enter the name of the second file: ')
#commenting this out to be able to run a tests
getFile1 = 'angles_UCI_CS.csv'
getFile2 = 'angles_UCI_CS_out.csv'

print(compareFiles(getFile1, getFile2))
