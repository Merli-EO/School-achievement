#!/bin/zsh

echo "Ceci est un Shell script qui permet de séparer exclusivement les données du WHAM"
echo " Veuillez saisir le nom de votre fichier"

read Data

sed -n '2,62p' $Data > set1_$Data
sed -n '64, 124p' $Data > set2_$Data
sed -n '126, 186p' $Data > set3_$Data



exit 0