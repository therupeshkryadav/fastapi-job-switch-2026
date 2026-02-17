# WAP to ask to enter names of three favourite movies and store them in a list.Then print the list.
movies = []
print("Enter the names of three favourite movies: ")
mov1 = input("Movie 1: ")
mov2 = input("Movie 2: ")
mov3 = input("Movie 3: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
# WAP to check whether a list contains a palindrome of elements  ( Hint : Use copy() method) 
list1 = [1, 2, 3, 2, 1]
print("list1: ", list1)
list2 = list1.copy()
list2.reverse()
if list1 == list2:
    print("The list is a palindrome.")
else:    print("The list is not a palindrome.")