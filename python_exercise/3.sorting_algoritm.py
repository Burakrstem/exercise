def selection_sort(data):
    for i in range (len(data)):
        min=i                          #set the first element as minimum
        for j in range(i+1,len(data)): #compare minimum with other element
            if data[j]<data[min]:      #if other element is smaller than minimum, asign it as minimum
                min=j                  #make it goes until last element
        data[i],data[min]=data[min],data[i]
    print(data)


def buble_sort(data):
    for i in range(len(data)):
        for j in range(0,len(data)-(i+1)): 
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
    print(data)    


def insertion_sort(data):
    for i in range(1,len(data)):
        key=data[i]
        j=i-1
        while j>=0 and key<data[j]:
            data[j+1]=data[j]
            j=j-1
        data[j+1]=key
    print(data)



if __name__=='__main__':
    data=[20,12,10,15,2]
    print("selection sort=",selection_sort(data))
    print("buble sort=",buble_sort(data))
    print("insertion sort=",insertion_sort(data))