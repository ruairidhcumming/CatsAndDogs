import os 
import shutil
i = 1 
path='../train/'
catdir = '../cat/'
dogdir = '../dog/'
for files in os.listdir('../train'):
    i=i+1
    src = path+files
   
    if (files[0]=='d'):
        print ('dog')
        dst=dogdir+files
    if (files[0]=='c'):
        dst = catdir+files
        print ('dog')
    shutil.move(src,dst)

    if i == 20 :break

    if i %100==0 : print (i)
    
print('DONE')