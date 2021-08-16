javac Main.java
java Main

for f in d*.dot; 
do dot -Txdot $f | dot2tex > $f.tex; done
for f in *.class;
do rm $f; done
python3 edit.py
for f in *.dot;
do rm $f; done