uses crt,sysutils,Classes,A3;
type CN=array[1..10] of Integer;
var	Counters1:CN=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
	Counters2:CN=(2, 2, 2, 2, 2, 2, 3, 1, 1, 0);
	Counters3:CN=(2, 2, 2, 2, 2, 2, 2, 2, 2, 3);
	Counters4:CN=(10, 1, 2, 3, 4, 5, 6, 7, 8, 9);
	Counters5:CN=(0, 1, 2, 3, 9, 5, 6, 7, 8, 9);
procedure StartTest(rez:Integer; Counters:CN;line:String);
begin
	if rez <>SearchMax(Counters) then
	begin
		Writeln('Module A3 '+line+' FAILED');
	end
	else
		Writeln('Module A3 '+line+' pass');

end;

begin
	
	StartTest(1,Counters1,'Test1');
	StartTest(7,Counters2,'Test2');
	StartTest(0,Counters3,'Test3');
	StartTest(1,Counters4,'Test4');
	StartTest(5,Counters5,'Test5');
	
end.