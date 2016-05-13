#!/bin/bash
DATE=`date +%Y-%m-%d-%H-%M-%S`

RED=`tput setaf 1`
NC=`tput sgr0`
mkdir $DATE
#  |tee -a  $DATE/report.txt  create file with stdout and print stdout to console

ls | grep '^in' | while read line
do
	#echo $line
	.././main< $line >$DATE/'out'$line |tee -a  $DATE/report.txt
	#echo diff $DATE/'out'$line answers/'out'$line |tee -a  $DATE/report.txt
	#diff $DATE/'out'$line answers/'out'$line |tee -a  $DATE/report.txt

	diff -q $DATE/'out'$line answers/'out'$line 1>/dev/null
	if [[ $? == "0" ]]
	then
  		echo "Test with file "$line" pass"  |tee -a  $DATE/report.txt
	else
 		echo "Test with file "$line" ${RED} FAILED${NC}"  |tee -a  $DATE/report.txt
		echo diff $DATE/'out'$line answers/'out'$line |tee -a  $DATE/report.txt
        	diff $DATE/'out'$line answers/'out'$line |tee -a  $DATE/report.txt

	fi
done

.././TestA1 <TestA1in.txt >$DATE/TestA1out.txt |tee -a  $DATE/report.txt
diff -q $DATE/'TestA1out.txt' answers/TestA1out.txt 1>/dev/null
if [[ $? == "0" ]]
then
	echo "Module A1 Test pass"  |tee -a  $DATE/report.txt
else
        echo "Module A1 Test  ${RED} FAILED${NC}"  |tee -a  $DATE/report.txt

fi

.././TestA2 | tee -a $DATE/report.txt
.././TestA3 | tee -a $DATE/report.txt
.././TestA21 | tee -a $DATE/report.txt
