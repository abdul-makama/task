print('GAME 1-15')
print('The program will ask you to choose a number in your mind ranging from 1-15, and tell you the  number you choosed')
print('choose a number under the range below')
game = range(16)
game = list(game[1:16])
print(game)
a = list(range(1,15,3))
b = list(range(2,15,3))
c = list(range(3,15,3))
print('Choose the number of row that the you chosen belong to')
print('row1:', a)
print('row2:', b)
print('row3:', c)
key1 = input('Enter the number of row: ')
key1 = int(key1)
if key1 == 1:
    row_a , row_b , row_c = a , b , c
    key_middle = row_c + row_a + row_b
    row_a2 = [15,6,10,1,8]
    row_b2 = [12,3,7,14,5]
    row_c2 = [9,13,4,11,2]
    print('row1: ',list(row_a2))
    print('row2: ',list(row_b2))
    print('row3: ',list(row_c2))
    print('choose a row, the number you choosed belonged to')
    skey_1_123 = input('Enter the number of row: ')
    skey_1_123= int(skey_1_123)
elif key1 == 2:
    row_a2 = [13,4,11,2,9]
    row_b2 = [10,1,8,15,6]
    row_c2 = [7,14,5,12,3]
    print('row1: ',list(row_a2))
    print('row2: ',list(row_b2))
    print('row3: ',list(row_c2))
    print('choose a row, the number you choosed belonged to')
    skey_2_123 = input('Enter the number of row: ')
    skey_2_123 = int(skey_2_123)
elif key1 == 3:
    row_a2 = [13,4,12,3,8]
    row_b2 = [10,1,9,14,5]
    row_c2 = [7,15,6,11,2]
    print('row1: ',list(row_a2))
    print('row2: ',list(row_b2))
    print('row3: ',list(row_c2))
    print('choose a row, the number you choosed belonged to')
    skey_3_123 = input('Enter the number of row: ')
    skey_3_123 = int(skey_3_123)
else:
    print('Sorry, invalid number of raw. Try again')
    skey_3 = int(skey_3)
if skey_1_123 == 1:
    skey_middle = row_a2 + row_b2 + row_c2
    row_a3 = [2,13,1,15,7]
    row_b3 = [11,9,10,5,3]
    row_c3 = [4,8,6,14,12]
    print('row1: ' ,row_a3)
    print('row2: ' ,row_b3)
    print('row3: ' ,row_c3)
    print('from the above choose the number of the that the number you have chosen belong to')
    gkey_1_1_123 = input('Enter the number of row: ')
    gkey_1_1_123 = int(gkey_1_1_123)
elif skey_1_123 == 2:
    skey_middle = row_a2 + row_b2 + row_c2
    row_a3 = [8,6,14,12,4]
    row_b3 = [1,15,7,2,13]
    row_c3 = [10,5,3,11,9]
    print('row1: ' ,row_a3)
    print('row2: ' ,row_b3)
    print('row3: ' ,row_c3)
    print('from the above choose the number of the that the number you have chosen belong to')
    gkey_1_2_123 = input('Enter the number of row: ')
    gkey_1_2_123 = int(gkey_1_2_123)
elif skey_1_123 == 3:
    skey_middle = row_a2 + row_b2 + row_c2
    row_a3 = [8,6,11,9,7]
    row_b3 = [1,15,4,5,3]
    row_c3 = [10,2,13,14,12]
    print('row1: ' ,row_a3)
    print('row2: ' ,row_b3)
    print('row3: ' ,row_c3)
    print('from the above choose the number of the that the number you have chosen belong to')
    gkey_1_3_123 = input('Enter the number of row: ')
    gkey_1_3_123 = int(gkey_1_3_123)
else:
    print('Sorry, invalid number of raw. Try again')
if gkey_1_1_123 == 1:
    ans = 1 
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
elif gkey_1_1_123 == 2:
    ans = 10 
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
elif gkey_1_1_123 == 3:
    ans = 6
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
else:
    print('Going to next step....')
if gkey_1_2_123 == 1:
    ans = 14
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
elif gkey_1_2_123 == 2:
    ans = 7 
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
elif gkey_1_2_123 == 3:
    ans = 3
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
else:
    print('Going to next step....')
if gkey_1_3_123 == 1:
    ans = 11
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
elif gkey_1_3_123 == 2:
    ans = 4
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
elif gkey_1_3_123 == 3:
    ans = 13
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
else:
    print('Going to next step....')
if skey_2_123 == 1:
    row_a3 = [3,14,2,13,8]
    row_b3 = [12,7,11,6,1]
    row_c3 = [5,9,4,15,10]
    print('row1: ' ,row_a3)
    print('row2: ' ,row_b3)
    print('row3: ' ,row_c3)
    print('from the above choose the number of the that the number you have chosen belong to')
    gkey_2_1_123 = input('Enter the number of row: ')
    gkey_2_1_123 = int(gkey_2_1_123)
elif skey_2_123 == 2:
    row_a3 = [9,4,15,10,5]
    row_b3 = [2,13,8,3,14]
    row_c3 = [11,6,1,12,7]
    print('row1: ' ,row_a3)
    print('row2: ' ,row_b3)
    print('row3: ' ,row_c3)
    print('from the above choose the number of the that the number you have chosen belong to')
    gkey_2_2_123 = input('Enter the number of row: ')
    gkey_2_123 = int(gkey_2_123)
elif skey_2_123 == 3:
    row_a3 = [9,4,12,7,15]
    row_b3 = [11,13,5,6,1]
    row_c3 = [2,3,14,8,10]
    print('row1: ' ,row_a3)
    print('row2: ' ,row_b3)
    print('row3: ' ,row_c3)
    print('from the above choose the number of the that the number you have chosen belong to')
    gkey_2_3_123 = input('Enter the number of row: ')
    gkey_2_3_123 = int(gkey_2_3_123)
else:
    print('Sorry, invalid number of raw. Try again')
if gkey_2_1_123 == 1:
    ans = 2
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
elif gkey_2_1_123 == 2:
    ans = 11
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
elif gkey_2_1_123 == 3:
    ans = 4
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
else:
    print('Going to the next step')
if gkey_2_2_123 == 1:
    ans = 15
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
elif gkey_2_2_123 == 2:
    ans = 8
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
elif gkey_2_2_123 == 3:
    ans = 1
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
else:
    print('Approaching the next step')
if gkey_2_3_123 == 1:
    ans = 12
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
elif gkey_2_3_123 == 2:
    ans = 5
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
elif gkey_2_3_123 == 3:
    ans = 14
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
else:
    print('Approaching the next step')
if skey_3_123 == 1:
    row_a3 = [2,15,3,13,9]
    row_b3 = [11,7,12,5,1]
    row_c3 = [6,8,4,14,10]
    print('row1: ' ,row_a3)
    print('row2: ' ,row_b3)
    print('row3: ' ,row_c3)
    print('from the above choose the number of the that the number you have chosen belong to')
    gkey_3_1_123 = input('Enter the number of row: ')
    gkey_3_1_123 = int(gkey_3_1_123)
elif skey_3_123 == 2:
    row_a3 = [8,4,14,10,6]
    row_b3 = [3,13,9,2,15]
    row_c3 = [12,5,1,11,7]
    print('row1: ' ,row_a3)
    print('row2: ' ,row_b3)
    print('row3: ' ,row_c3)
    print('from the above choose the number of the that the number you have chosen belong to')
    gkey_3_2_123 = input('Enter the number of row: ')
    gkey_3_2_123 = int(gkey_3_2_123)
elif skey_3_123 == 3:
    row_a3 = [8,4,11,7,9]
    row_b3 = [3,13,6,5,1]
    row_c3 = [12,2,15,14,10]
    print('row1: ' ,row_a3)
    print('row2: ' ,row_b3)
    print('row3: ' ,row_c3)
    print('from the above choose the number of the that the number you have chosen belong to')
    gkey_3_2_123 = input('Enter the number of row: ')
    gkey_3_2_123 = int(gkey_3_2_123)
else:
    print('Sorry, invalid number of raw. Try again')
if gkey_3_1_123 == 1:
    ans = 3
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
elif gkey_3_1_123 == 2:
    ans = 12
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
elif gkey_3_1_123 == 3:
    ans = 4
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
else:
    print('Going to the next step')
if gkey_3_2_123 == 1:
    ans = 14
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
elif gkey_3_2_123 == 2:
    ans = 9
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
elif gkey_3_2_123 == 3:
    ans = 12
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
else:
    print('Almost done')
if gkey_3_3_123 == 1:
    ans = 11
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
elif gkey_3_3_123 == 2:
    ans = 6
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
elif gkey_3_3_123 == 3:
    ans = 15
    print('Loading.....')
    print('Executing...')
    print('the number you have chosen in your mind is ',ans)
else:
    print('Sorry, your process was wrong. Try again')
    
    

    

    
  


