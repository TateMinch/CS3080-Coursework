#!/bin/bash

loseCount=0

for i in {1..10000}
do
out=$(python3 hw2_tate_minch_ex_4_3.py | grep 'Sorry, the number I was thinking')
    if [ -n "$out"  ];
    then
        ((loseCount=loseCount+1))
    fi
done
echo $loseCount


