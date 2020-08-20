awk '{for(i=1;i<=NF;i++){asso_array[$i]++;}};END{for(w in asso_array){print w,asso_array[w];}}' words.txt | sort -rn -k2

# cat words.txt | xargs -n1 | sort | uniq -c | sort -rn | awk '{print $2,$1}'