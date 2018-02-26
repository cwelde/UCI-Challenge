cwd=$(pwd)
input="$cwd/angles/UCI_CS.csv"
output="$cwd/output.csv"

#downloading csv
sh tst/tst_dwnl.sh



#Run cosine calculating program
python ./src/compute_cosines.py


#Run comparison program

python ./tst/tst_comp_csv.py
