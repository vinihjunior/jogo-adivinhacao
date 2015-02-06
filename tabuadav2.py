#  *Tabuada version 2
#  *data 08/12/14 
#  *@author Vinicius Junior


mult, var, cont  = 1, 0, 0

while cont <= 10:
    print (mult,"x",var,'=',mult*var)
    var = var + 1
    cont = cont + 1
    if (cont >= 11):
        mult = mult + 1
        if mult <= 10:
            var = var   - 11
            cont = cont - 11
            


    
