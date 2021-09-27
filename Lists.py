# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 19:13:30 2021

@author: Nikhil J
@autor_email:se.nikhilj45@gmail.com
"""
# Data Structure Lists
# Features of Lists > Order is everything > Mutable > Heterogenous data > Multiple Entry > Iterable 

ls_1 =[12,13,17,14,15,16,17,17]
ls_2 =[19,20]
ls_0 =[*range(11,21)] # creating  list using range function and the last number specified in range will not be included
ls_01=[34,56,78,32,14,67,90,45,67,90,58,94,84,30,13,32,30,39,67]
# Add items to the list

ls_1.append(18) # add number at end of list >>> mutation possible
ls_1.insert(0,11) # adds specified value at specified index and shift the data resulting in increase of size by +1
ls_1.extend(ls_2) # merge other list into ls_1 meanwhile >>>>>>>> "PRESERVING ORDER" 

ls_3 = ls_1 + ls_2 # joining two lists / concatenations
ls_4 = [ls_1,ls_2,ls_3] # lists in lists 

# Removal from list 
ls_1.remove(17) # remove the specified value contained in list
# if list has multiple objects of same value it removes only one with lower index in +ve index
# if not a multiple entry in +ve index then beginning lower numerical from -ve index
ls_1.pop(-4) # Removal from index specified

# Slicing and Selection

ls_5=ls_1[0:4] # slices ls_1 for given index range 0,1,2,3 __it doesnt slices the index specified at the end i.e 4 
print(ls_1) # SInce we sliced the list1 in last line but the list used for slicing dont go anychanges

# clear a list
ls_5.clear() # transforms a list into empty list [] !!!!
del(ls_5)    # deletes a list

# sort a list >>>>>>>>>>>>> ls_var.sort ( reverse = False) >>> default: Ascending
ls_01.sort() # look ls_01 is sorted ascneding
ls_01.sort(reverse = True) # look ls_01 is sorted descending

# Count in list
ls_01.count(67) # count the number of occurences of number specified

from collections import Counter
print(Counter(ls_01)) #creates a dictionary with the key the objects and gives the values as no of occurances
# also sorts accorfing to max number of occurances taken first

# Alternate way to use counter

_count = Counter()   # intialize the counter
_count.update(ls_01) # update the counter 
print('%d : %d' % (67, _count[67])) 




# __________<<<<<<<<< LIST COMPREHENSION >>>>>>>>>>>>>___________________#

# <<<<<<< COMPLEX FUNCTIONS ON LISTS >>>>>>>>>>>>>>>>>>>>>>>

# [ expr for val in collection ]
# [ expr for val in collection  if < test >]
# [ expr for val in collection if < test 1 > and < test 2 >]
# [ expr for val1 in collection1 and val2 in collection2 ]

# Task 1 : Create a list of remainders of numbers from range(a,b) by a number "n"
# here my range is first 100 numbers divided by 11

p_rem = [x % 11 for x in range (1,101)]
p_rem
print(Counter(p_rem))

# Task 2 : Create a list of remainders of squared numbers from range(a,b) by a number "n"
# here my range is first 100 numbers divided by 11
# length of list formed by dividing square of first n natural numbers by p will give (p+1)/2 remainders type


sq_rem =[x**2%11 for x in range(1,101)]
sq_rem
print(Counter(sq_rem))
# here we got (11+1)/2 type of remainders :6 remainder viz 1,4,9,5,3,0 total 6 

# Task 3: Sort theNames of author list by their <Last Names>  both ways using functions

authors=["Issac Newton","Thomas Beckett","Johnnie Walker","Rudyard Kipling","Annie Bessant","Mahatma Gandhi","Oprah Winfrey"]

# Using inbuilt function Sort
authors.sort(key= lambda name: name.split(" ")[-1].lower()) # sorted with last name ascending order 
authors
authors.sort(key= lambda name:name.split(" ")[0].lower())   # # sorted with first name ascending order
authors
authors.sort(key= lambda name: name.split(" ")[-1].lower(),reverse=True) # sorted with last name descending order 
authors
authors.sort(key= lambda name:name.split(" ")[0].lower(),reverse=True) # sorted with first name descending order
authors
# Task 4: Given the list of radii , Find the area and circumference
radii =[1,2,3,4,5,6,7]
import math
d =2
# Method 1 : By  defining a function area
def area (r):
    return math.pi * (r**2)
def circ (r):
    return math.pi * d * r
areas =[] # Declaring an empty list areas
for r in radii:
    a=area(r)
    areas.append(a)
print(areas)
circums=[]
for r in radii:
    c=circ(r)
    circums.append(c)
print(circums)
# Method 2: Using Map function >>>>> map(function,iterables)
areas_2 = list( map(area,radii))
circum_2= list(map(circ,radii))
# Method 3: Using Anonymous map
areas_3 = list(map(lambda x: math.pi * (x**2),radii))
circum_3 = list ( map (lambda x:math.pi * 2 *x, radii))

if circums == circum_2 and circum_2 == circum_3:
   print("They are Equal")
if areas == areas_2 and areas_2 == areas_3:
   print("They are Equal")
#__________________Task 3 ends_______________
# Task 4 : Lists of Cities and their temperatures are supplied in list of tuples. Convert them to Faren and print list
temps = [("Delhi",29),('Kanpur',32),('Nagpur',40),('Chandrapur',47)]

# Method 1 :>>>>>>>>
def c2t (f):
    return 1.8*f +32
resf=[l[1] for l in temps]
names=[l[0] for l in temps]
resc=[c2t(i) for i in resf]
for i in range(4):
    temps_conv3= [(names[i],resc[i])]
    print(temps_conv3)
def merge(l1,l2):
    return list(map(lambda x,y:(x,y),l1,l2))
temp_conv=merge(names,resc)
print(temp_conv)
# Method 2 : >>>>>>>
c_2_f = lambda l:([l[0],1.8*l[1] +32])
temp_conv2 = list (map (c_2_f,temps))
print(temp_conv2)

# TASK 5 : For the given list of marks find the average and filter the list of below avg and above average
marks=[45,56,67,89,30,99,77,40,59,38]
import statistics as ss
avg = ss.mean(marks)
print('The Average Mark is',avg)
# Method 1
tot_marks = sum(marks)
tot_obser = len(marks)
tot_avg   = tot_marks/tot_obser
m_up=[]
m_do=[]
for i in range(10):
    if marks[i] < avg: 
       m_do.append(marks[i])
    else:
        m_up.append(marks[i])
print('The above avg mark list ',m_up)
print('The Below avg mark list',m_do)

# Method 2
abov = list ( filter ( lambda x: x >avg, marks))
belo = list ( filter ( lambda x: x < avg, marks))

# Task 6 : List over the squares for first 100 numbers
squares=[]
for i in range(1,101):
    squares.append(i**2)
print(squares)
squares2=[x**2 for x in range(1,101)]

# Task 6: Following is list of movies. Compute:
movie = [" Rose Capablanca","Bobby Fischer","Antony Polyakov","Mikhail Tal","Gandhi","Star Wars","Alice in Wonderland",
         "Ginger","Grims of Life","Titanic","Sicarios","Garbage Yard","Gabriel Shot","General Motors","Grand City",
         "Gangs of Wasseypur","Ganges","Guru","Go Goa Gone","Inception","Indiana Los"]
# Print all Movies starting with G
Gmovies =[]
for title in movie:
    if title.startswith("G"):
        Gmovies.append(title)
print (Gmovies)
# with >>>>> LIst comprehension
Gmov=[title for title in movie if title.startswith("G")]
movies = [(" Rose Capablanca",1940),("Bobby Fischer",1995),("Antony Polyakov",1945),("Mikhail Tal",1970),("Gandhi",2001),("Star Wars",2005),("Alice in Wonderland",2010),
         ("Ginger",1999),("Grims of Life",2014),("Titanic",1980),("Sicarios",2015),("Garbage Yard",2016),("Gabriel Shot",2019),("General Motors",2013),("Grand City",2020),
         ("Gangs of Wasseypur",2015),("Ganges",2006),("Guru",2005),("Go Goa Gone",2015),("Inception",2003),("Indiana Los",2016)]
# Give only the names of movies that were before 1990 
# Give another list the names after 2000
m_b4 =[title for (title,year) in movies if year <1990]
m_b4
m_af = [title for (title,year) in movies if year>2000]
# Can also return the name with year after 2000
m_g = [(title,year) for (title,year) in movies if year > 2000 ]
