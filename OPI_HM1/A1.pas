{$INCLUDE directive.txt}
{	Read user input to matrix.
	@author(Medvedev Alexey)
	@lastmod(2016/05/13 22:15:00)	
}
unit A1;

interface

uses
  Classes, SysUtils;
type
{ 
	Matrix 100x100 of integer
}
	Mat=array[1..100] of array[1..100] of Integer;

{
 Read user input to matrix. Call procedure as ReadMatrix(10,10,Matrix);
 @param(Width  Integer, width of matrix)
 @param(Height  Integer, height of matrix)
 @param(Matrix  Array 100x100 of integer where saved user matrix)
}

procedure ReadMatrix(Width:Integer;Height:Integer;var Matrix:Mat);

implementation

procedure ReadMatrix(Width:Integer;Height:Integer;var Matrix:Mat);
var
  I, J : integer;
begin

	Assert(Height>0);
	Assert(Width> 0);
	for I:=1 to Height do
		begin
			for J := 1 to Width do
			begin
				Read(Matrix[I,J])				
			end;
		end;
end;

end.

