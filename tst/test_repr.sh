


#Get CSV files
sh tst/tst_dwnl.sh



#Run cosine calculating program
python ./src/compute_cosines.py


#Run comparison program

python ./tst/tst_comp_csv.py
