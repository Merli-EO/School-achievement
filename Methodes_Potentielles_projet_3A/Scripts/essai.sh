#!/bin/zsh

echo "ici on essai un truc :)"
echo " quel est ton fichier ? :)"

read file


long=$(wc -l $file )

echo "ton fichier contient:" $long "lignes"

div1=$(( $long/3 ))
div2=$(( 2*$div1))
div3=$(( $long ))

sed -n '2,$(div1)p' $file | sed -n 's/E/e/g' > set1_$file
sed -n '$(($div1 +2)),$(div2)p' $file | sed -n 's/E/e/g' > set2_$file
sed -n '$(($div2 +2)),$(div3)p' $file | sed -n 's/E/e/g' > set3_$file

exit 0
