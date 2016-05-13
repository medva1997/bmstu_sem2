{$INCLUDE directive.txt}

uses crt,sysutils,Classes,A1,A2,A3;
var Height, Width,N,I,J,Len:Integer;
	Matrix:array[1..100] of array[1..100] of Integer;
	Counters: A2.CN;

procedure PrintN(N:Integer);
begin
	writeln('Максимально повторяющаяся цифра: ',N);
end;

begin
	{$ifdef DEBUG}
  	//WriteLn('Debug version');
	{$endif}
	
	write('Введите высоту матрицы: ');
	Read(Height);
	write('Введите ширину матрицы: ');
	Read(Width);
	if (Height>100)or(Height<1)or(Width>100) or (Width<1) then
	begin
		writeln('Error1: Размер матрицы введен неверно.');
		Exit;
	end;

	//Read matrix
	writeln('Введите эллементы матрицы: ');
	ReadMatrix(Width,Height, Matrix);

	//Print matrix
	writeln('Матрица: ');
	for I:=1 to Height do
		begin
			for J := 1 to Width do
			begin
				write(Matrix[I,J]);
				write(' ');			
			end;
			writeln;
		end;

	SearchInclusions(Width,Height,Matrix,Counters);


	N:=SearchMax(Counters);
	Assert(N<10);
	PrintN(N)
end.