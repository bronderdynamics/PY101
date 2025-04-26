#Exercise 1
#I would use the len function len(people)

#Exercise 2
#tuples aren't mutable. I would either make a new one or overwrite the current

#Exercise 3
#lists are mutible but tuples are not
#you define a list with [] and tubles with ()
#they are both sequences and heteogeneous

#Exercise 4
#strings have an index

#Exercise 5
#sets are unordered and cannot be indexed

#Exercise 6
pi = 3.141592
str_pi = str(pi)

#Exercise 7
#range(7) = 0 1 2 3 4 5 6
#range(1, 6) = 1 2 3 4 5
#range(3, 15, 4) = 3 7 11 15
#range(3, 8, -1) = null
#range(8, 3, -1) = 8 7 6 5 4

#Exercise 8
print(list(range(3, 17, 4)))

#Exercise 9
#yes
#no they are different objects
#yes
#yes

#Exercise 10
#no because it is a set and unordered

#Exercise 11
which_country = {
    "Alice":"USA",
    "Francios":"Canada",
    "Inti":"Peru",
    "Monika":"Germany",
    "Sanyu":"Uganda",
    "Yoshitaka":"Japan"
}

print(which_country["Alice"])