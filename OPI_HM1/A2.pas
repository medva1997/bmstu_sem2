unit A2;

interface

uses
  Classes, SysUtils,A21;
type
	Mat=array[1..100] of array[1..100] of Integer;
	CN=array[1..10] of Integer;
	TIntMassiv = array of Integer;

procedure SearchInclusions(Width:Integer;Height:Integer;Matrix:Mat );

implementation

procedure SearchInclusions(Width:Integer;Height:Integer;Matrix:Mat);

var
  I, J,K: integer;
  Numbers: array of Integer;
  Counts:array[1..11] of Integer;
begin
	for I:=1 to Height do
	begin
		for J := 1 to Width do
		begin
			Setlength(Numbers,1);
			//ConvertNumToFig(Matrix[I][J],Numbers);
			for K := 0 to Length(Numbers) do
			begin
				if Numbers[k]<>0 then
					Сounts[Numbers[k]]:=Сounts[Numbers[k]]+1	
				else
					Сounts[10]:=Сounts[10]+1;				
			end;								
		end;
	end;
	
end;
end.