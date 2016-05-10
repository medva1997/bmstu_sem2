{$INCLUDE directive.txt}
unit A1;

interface

uses
  Classes, SysUtils;
type
	Mat=array[1..100] of array[1..100] of Integer;
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

