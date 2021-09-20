import random;
import time;

def partition(listToBeSorted, start, end):
    i = (start-1);
    pivot = listToBeSorted[end];
    for j in range(start, end):
        if listToBeSorted[j] <= pivot:
           i += 1;
           listToBeSorted[i], listToBeSorted[j] = listToBeSorted[j], listToBeSorted[i];
    i+=1;
    listToBeSorted[i], listToBeSorted[end] = listToBeSorted[end], listToBeSorted[i];
    return i;

def partition_random(listToBeSorted, start, end):
    index = random.randint(start, end);
    listToBeSorted[index], listToBeSorted[end] = listToBeSorted[end], listToBeSorted[index];
    return partition(listToBeSorted, start, end);

def quickSort(listToBeSorted, start, end, useRandom):
    if len(listToBeSorted) == 1:
        return listToBeSorted;
    if start < end:
        if useRandom:
            p = partition_random(listToBeSorted, start, end)
        else:
            p = partition(listToBeSorted, start, end);
        quickSort(listToBeSorted, start, p-1, useRandom);
        quickSort(listToBeSorted, p+1, end, useRandom);
    
def getInputs():
    n = int(input("How many random values to sort(should be less than 1000)? "));
    randomList = random.sample(range(0, 1000), n);
    for i in range(len(randomList)):
        givenList.append(randomList[i]);

def displayResult():
    print("\n\nRandomly generated list: ", givenList);
    print("\nList sorted without randomization: ", sortedList);
    print("\nList sorted with randomization: ", sortedList2);
    print("\nTime to sort without random: ", withoutRandom);
    print("\nTime to sort with random: ", withRandom);

#Get inputs    
n = 0;
givenList = [];
getInputs();
sortedList = givenList.copy();
sortedList2 = givenList.copy();

#Sort without randomization
start_time = time.time();
quickSort(sortedList, 0, len(givenList) - 1, False);
withoutRandom = time.time() - start_time;

#Sort without pivot = last element
start_time2 = time.time();
quickSort(sortedList2, 0, len(givenList) - 1, True);
withRandom = time.time() - start_time;

#Display results
displayResult();
