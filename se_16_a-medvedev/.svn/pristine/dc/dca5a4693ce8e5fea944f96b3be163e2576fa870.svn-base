uses crt,sysutils,Classes,A1;
var Height, Width,N,I,J:Integer;
	Matrix:array[1..100] of array[1..100] of Integer;
	OutMatrix1:array[1..2] of array[1..3] of Integer=((1,2,3),(4,5,6));
	OutMatrix2:array[1..3] of array[1..3] of Integer=((12,23,34),(45,56,-67),(77,8,9));
	flag:Boolean;
begin

	//test1
	flag:=false;
	Width:=3;
	Height:=2;
	ReadMatrix(Width,Height, Matrix);	
	for I:=1 to Height do
		begin
			for J := 1 to Width do
			begin
				if Matrix[i][j]<>OutMatrix1[i][j] then
				begin
				writeln(Matrix[i][j],i,j);
				flag:=True;					
				end;							
			end;
		end;
	if flag=True then writeln('Test 1 failed')
	else writeln('Test 1 passed');

	//test2
	flag:=false;
	Width:=3;
	Height:=3;
	ReadMatrix(Width,Height, Matrix);	
	for I:=1 to Height do
		begin
			for J := 1 to Width do
			begin
				if Matrix[i][j]<>OutMatrix2[i][j] then
				begin
				writeln(Matrix[i][j],i,j);
				flag:=True;					
				end;							
			end;
		end;
	if flag=True then writeln('Test 2 failed')
	else writeln('Test 2 passed')
end.