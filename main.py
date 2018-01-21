'''
Created on Jan 21, 2018

@author: Sourcode
'''

import numpy as np
import _csv
import os

def main():
    pin_status = 1
    flag = False
    filename = 'test.txt'
    
    #read the file
    r_file = open(filename, 'r')
    reader = _csv.reader(r_file, delimiter=',')
    if os.stat(filename).st_size == 0:
        print('file empty')
        return 0
    #endif
    
    data = []
    
    for row in reader:
        data.append(row[0])
    #next
    
    r_file.close()
    
    i_data = int(data[0])    
    
    #Check the status and write to the file
    w_file = open(filename, 'w')
    
    if pin_status == 1:
        flag = True
    elif pin_status == 0:
        flag = False
    #endif
    
    if flag == True:
        if i_data == 1:
            w_file.write('0')
            print('0')
        elif i_data == 0:
            w_file.write('1')
            print('1')
        #endif
    else:
        w_file.write(str(i_data))
        print(str(i_data))
    #endif
    
    w_file.close()
        
    return

if __name__ == '__main__':
    main()
    
