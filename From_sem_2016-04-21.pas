{
Дана строка целых чисел. N чисел.  Из конца сдвинуть K элементов вперед.
1 2 3 4 5 6 7 8
6 7 8 1 2 3 4 5   
}


program untitled;

uses crt;
const n=10;
var i,k,temp: integer;
	Arr:array [1..n] of integer;

BEGIN
writeln('Введите K');
readln(k);

for i:=1 to n do     	
	Arr[i]:=i;

for i:=1 to k do
begin
	temp :=Arr[i];
	Arr[i]:=Arr[n-k+i];
	Arr[n-k+i]:=temp; 
end;
		

for i:=1 to n do	
	write(Arr[i],' ');	
	
END.

