INPUTFILE=http://rapid-hub.org/data/angles_UCI_CS.csv
OUTPUTFILE=http://rapid-hub.org/data/angles_UCI_CS_out.csv

curl -fsS -o angles_UCI_CS.csv $INPUTFILE
curl -fsS -o angles_UCI_CS_out.csv $OUTPUTFILE
