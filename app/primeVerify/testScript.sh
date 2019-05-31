echo "RESULTADOS DE ALGORITMO PRIMOS"
echo "------------------------------"
echo "------------------------------"

rm -rf machines && sed -e 's/#.*//' -e 's/[[:blank:]]*$//' -e '/^$/d' -e '/^f/d' -e '/^:/d' -e '/^127/d' /etc/hosts | awk '{print $1, "\t", "slots=4 max-slots=4"}' >> machines && sort -u machines

echo "------ TEST BEGINS -----------"
for cores in {2..16..2}
do
echo "----------------------------------"
echo "Numero de cores funcionando -->"  $cores
	for n in {2..8..2}
	do
	 echo "Longitud de primos -->"  $n
	 mpiexec -n $cores --hostfile machines python $1 $n
	done
done

echo "--------------------------------"
echo "---------------END--------------"
