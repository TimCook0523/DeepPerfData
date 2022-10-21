#!/bin/bash
if [ ! -d $1_data_parts ]; then
    mkdir $1_data_parts
fi
lc=`cat $1_SCP.txt | wc -l`
echo $lc
let pc=lc/20
i=1
while [ $i -le 20 ]; do
    let s=(i-1)*pc+1
    let e=i*pc
    if [ $i -eq 20 ]; then
        sed -n "${s}, \$p" $1_SCP.txt > $1_data_parts/$1_$i.txt
    else
        sed -n "${s},${e}p" $1_SCP.txt > $1_data_parts/$1_$i.txt
    fi
    let i++
done