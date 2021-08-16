javac Main.java
java Main

for f in *.tex; 
do rm $f; done

COUNTER=1
TITLE='H13_tree'

for f in d*.dot; 
do dot -Txdot $f | dot2tex > $TITLE$COUNTER.tex; COUNTER=$((COUNTER+1)); done
#do dot -Txdot $f | dot2tex > $TITLE$COUNTER.tex; rm $f; COUNTER=$((COUNTER+1)); done

for f in *.class; 
do rm $f; done
python3 edit.py