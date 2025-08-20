#activity 1
my_set = {1, 2, 3}
print(my_set)

my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

my_set = set([1, 2, 3, 2])
print(my_set, "\n")

num_set = set([0, 1, 3, 4, 5])
print("original set:")
print(num_set)
num_set.pop()
print("after removoing the first element from the set")
print(num_set, "\n")

#activity 2
setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)

#activity 3
import array as arr 

array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
print("original arry:"+str(array_num))

print("number of occurrences of the number 3 in the said array:"+str(array_num.count(3)))

array_num.reverse()
print("reversethe order of the times:")
print(str(array_num))

