#!/bin/bash

a=2
b=2
c=$((a + b))

mylist=(user1,user2,user3)

echo "Bash says: Hello, World!"
echo "$a + $b + $c"

for i in {1..3}
do 
	echo mylist
done
