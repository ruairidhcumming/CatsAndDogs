import os 
import shutil
i = 0
path='../train/Cats'
catdir = '../validate/Cats/'
dogdir = '../validate/Dogs/'
for files in os.listdir(path):
    i=i+1
    src = path+'/'+files
   
    if (files[0]=='d'):
       
        dst=dogdir+files
    if (files[0]=='c'):
        dst = catdir+files
       
    shutil.move(src,dst)
    if i%100 ==0: print(i)
   

    if i == 2500: break
path='../train/Dogs'
i=0
for files in os.listdir(path):
    i=i+1
    src = path+'/'+files
   
    if (files[0]=='d'):
       
        dst=dogdir+files
    if (files[0]=='c'):
        dst = catdir+files
       
    shutil.move(src,dst)

   
    if i%100 ==0: print(i)
    if i == 2500: break
print('DONE')