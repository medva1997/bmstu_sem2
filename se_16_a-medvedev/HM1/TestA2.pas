uses crt,sysutils,Classes,A2;
type CN=array[1..10] of Integer;
var Height, Width,I:Integer;
	Matrix:array[1..100] of array[1..100] of Integer;
	Counters: array[1..10] of Integer;
	OutCounters1:CN=(1, 1, 1, 1, 1, 1, 0, 0, 0, 0);
	OutCounters2:CN=(1, 2, 2, 2, 2, 2, 3, 1, 1, 0);

procedure StartTest(OutCounters:CN;line:String);
begin
	SearchInclusions(Width,Height,Matrix,Counters);
	
	for I:=1 to 10 do 
	begin
		if Counters[i]<>OutCounters[i] then
		begin
			Writeln('Module A2 '+line+' FAILED');
			break
		end;
	end;
			
	if I=10 then
	begin
		Writeln('Module A2 '+line+' pass');
	end;

	for  I := 1 to 10 do
	begin
		Counters[i]:=0;
	end;
end;

procedure Test1();
begin
	Width:=3;
	Height:=2;
	Matrix[1][1]:=1;
	Matrix[1][2]:=2;
	Matrix[1][3]:=3;
	Matrix[2][1]:=4;
	Matrix[2][2]:=5;
	Matrix[2][3]:=6;
	
	StartTest(OutCounters1,'Test1')
end;

procedure Test2();
begin
	Width:=3;
	Height:=3;
	Matrix[1][1]:=12;
	Matrix[1][2]:=23;
	Matrix[1][3]:=34;
	Matrix[2][1]:=45;
	Matrix[2][2]:=56;
	Matrix[2][3]:=-67;
	Matrix[3][1]:=77;
	Matrix[3][2]:=8;
	Matrix[3][3]:=9;

	StartTest(OutCounters2,'Test2')
end;



begin
	Test1();
	Test2();
end.