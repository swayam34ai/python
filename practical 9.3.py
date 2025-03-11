def create_array(a1,a2,a3,value):
    array=[]
    for i in range(a1):
        layer = []
        for j in range(a2):
            row = [value] * a3  
            layer.append(row)     
        array.append(layer)        
    return array
array=create_array(3,3,3,5)
for layer in array:
    for row in layer:
        print(row)
