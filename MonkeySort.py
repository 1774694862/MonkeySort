import random
import time

def Monkey_sort(sum):
    unsorted = [int(item) for item in range(int(sum))]
    unsorted[0]=sum
    ans=0
    def isSorted(collection):
        if len(collection) < 2:
            return True
        for i in range(len(collection) - 1):
            if collection[i] > collection[i + 1]:
                return False
        return True

    while not isSorted(unsorted):
        random.shuffle(unsorted)
        ans+=1
        print("第%d次猴子排序："%ans,end="")
        print(unsorted)
    avg=1
    for i in range(1,sum+1):
        avg*=i
    print("理论上进行%d次猴子排序。"%avg )
    print("而你进行了%d次猴子排序。"%ans)
    return ans

if __name__ == "__main__":
    # user_input = input("Enter a number to indicate that there are several numbers to MonkeySort :\n")
    start = time.time()
    user_input=5
    k=Monkey_sort(user_input)
    print(time.time()-start)
