#批量重命名文件

import os
path = 'd:\\fff\\pil\\img\\'
k=0
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        if file.find('.')>0:
            k+=1
            newname=os.path.join(path,str(k)+'.jpg')
            os.rename(os.path.join(path,file),newname)

            
