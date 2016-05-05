

uses crt,sysutils,Classes,A1,A2;
var Height, Width,N,I,J:Integer;
	Matrix:array[1..100] of array[1..100] of Integer;
	Counters: array[1..10] of Integer;
begin
	Read(Height);
	Read(Width);
	if (Height>100)or(Height<1)or(Width>100) or (Width<1) then
	begin
		writeln('Error1: Размер матрицы введен неверно.');
		Exit;
	end;
	ReadMatrix(Width,Height, Matrix);
	for I:=1 to Height do
		begin
			for J := 1 to Width do
			begin
				write(Matrix[I,J]);
				write(' ');			
			end;
			writeln;
		end;
	SearchInclusions(Width,Height,Matrix,Counters)
	//N:=SearchMax(Counters)
	//PrintN(N)
end.