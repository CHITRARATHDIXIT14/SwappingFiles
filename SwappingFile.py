file= input('Enter name of the first file :-      ')
file1 = input('Enter name of the second file :-   ')

def swapp() :
    with open(file , 'r') as a :
        data_a = a.read()
    with open(file , 'w') as a :
        a.write(data_b)
    with open(file1 , 'r') as b :
        data_b = b.read()
    with open(file1 , 'w') as b :
        b.write(data_a)
   
    

swapp()
    