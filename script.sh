#!/bin/bash

rm -f resultados.txt

for i in {1..64}
do
   echo -n "$i " >> resultados.txt
   ./tlb $i 100 >> resultados.txt
done

