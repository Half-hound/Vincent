food = ["steamedegg","boiledegg","scrambledegg","friedegg","rawegg"]
print(food[1])
print(food[-1])
food.append("omelet")
food.insert(0,"apple")
food.remove("boiledegg")
"""
I encountered this error:
"ValueError: list.remove(x): x not in list
I originally wrote: food.remove(2)
I thought I should use the item index. I fixed it by using the specific value.
"""
print(len(food))
"""
I encountered this error:
"SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
I originally wrote: print len(food)
I forgot the parenthesis. I fixed it by adding () around len(food).
"""
for item in food:
    print(item.upper())
"""
I encountered this error:
<built-in method upper of str object at 0x0000017527ED5080>
I originally wrote: print(item.upper)
I added parentheses to the end.
"""
slicedfood = food[0:6:5]
print (slicedfood)

yespotato=0
for item in food:
    if item == "potato":
        yespotato=yespotato+1
if yespotato>0:
    print("A potato!")
else: 
    print("No potato!")

liiist = range(0,21)
def get_first_15(numbers):
    return numbers[0:15]
def get_every_5th(liist):
    return get_first_15(liist)[::5]
def reverse_and_stride(lst):
    return (get_every_5th(lst)[::-1])[::3]
print (list(reverse_and_stride(liiist)))


list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]
numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
print(numbers[2])
print(numbers[1][1])
numbers.append([10,11,12])
def sum_nested(lste):
    sum=0
    for item in lste:
        for num in item:
            sum=sum+num
    return sum

print(sum_nested(numbers))

def creategrid (fxf):
    lst=range(0,26)
    num=1
    res=[]
    for row in range(5):
        sublist=[]
        for col in range(5):
            sublist.append(lst[num])
            num=num+1
        res.append(sublist)
    return res
fx=0
res=creategrid (fx)

def multiples (lst):
    res=[]
    for row in lst:
        sublist=[]
        for col in row:
            if col%3==0:
                sublist.append("?")
            else:
                sublist.append(col)
        res.append(sublist)
    return res
res=multiples(res)
print(res)

def sum(lst):
    sum=0
    for item in lst:
        for num in item:
            if num!="?":
                sum=sum+num
    return sum
res=sum(res)
print(res)


ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
    }
print (ages["Katie"])
ages["Mira"]=100
ages["Milana"]=52
del ages["Mariam"]
for person,old in ages.items():
    print (person, old)