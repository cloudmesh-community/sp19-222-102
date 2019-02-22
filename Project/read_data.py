import csv
import numpy as np
import matplotlib.pyplot as plt

def read(fpath): #function reads fpath and stores data in d
   d =[]
   var_name= [] # columns titles saved
   boolean=False
   with open(fpath) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter= ',')
      line_count=0
      for row in csv_reader:
         if line_count == 0:
           # print(f'Column names are {", ".join(row)}')
            var_name.append(row)
            line_count += 1
         else:
            for i in range(8):

               #print(type(row[i]))

               if(row[i]=="nan"):
                  boolean=True
                  break
            if(boolean==True):
               boolean=False
               continue
            else:
               d.append(row)
            #print(f'\t{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]} {row[7]} {row[8]}.')
            line_count +=1
   return d #d is an array of the rows read in. d[0]=colunmn titles. d[0][0]= first element in the first row

def format(d): #formats the data for easy integration
   N= len(d) #size of d
   n= len(d[0]) #should be equal to 8 aka numbers of columns in a row
   features= np.zeros((N,n-1)) #excludes last column due to that being the type
   labels= np.zeros(N)
   for k in range(N):

      labels[k] = d[k][8]
      for i in range(n-1):
         features[k,i] = d[k][i]
   return labels, features

print("hey")
d=read('Subject_53.csv')
print("Before deletion:", len(d))
labels, features = format(d)
print("after deletion:", len(labels))
#print(labels)

   