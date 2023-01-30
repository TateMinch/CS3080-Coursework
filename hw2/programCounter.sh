#!/bin/bash

lostCount=0

for i in {1..10000}
do
    python3 hw2_tate_minch_ex_4_3.py | grep 'Sorry, the number I was thinking'
done


