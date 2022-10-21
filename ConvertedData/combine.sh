#!/bin/bash
i=1
while [ $i -le 20 ]; do
    cat $1_data_parts/$1_$i.txt >> $1_SCP.txt
    let i++
done