DATE=`date +%Y-%m-%d-%H-%M-%S`
mkdir $DATE
#  |tee -a  $DATE/report.txt  create file with stdout and print stdout to console

ls | grep '^in' | while read line
do
	#echo $line
	.././main< $line >$DATE/'out'$line |tee -a  $DATE/report.txt
	echo diff $DATE/'out'$line answers/'out'$line |tee -a  $DATE/report.txt
	diff $DATE/'out'$line answers/'out'$line |tee -a  $DATE/report.txt
done

.././TestA1 <TestA1in.txt >$DATE/TestA1out.txt |tee -a  $DATE/report.txt
echo diff $DATE/'TestA1out.txt' $line answers/TestA1out.txt |tee -a  $DATE/report.txt
diff $DATE/'TestA1out.txt' $line answers/TestA1out.txt |tee -a $DATE/report.txt

.././TestA2 | tee -a $DATE/report.txt
.././TestA3 | tee -a $DATE/report.txt
.././TestA21 | tee -a $DATE/report.txt
