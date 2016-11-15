unit A2;

interface

uses
  Classes, SysUtils,A21;
type
	Mat=array[1..100] of array[1..100] of Integer;
	CN=array[1..10] of Integer;
	TIntMassiv = array of Integer;

procedure SearchInclusions(Width:Integer;Height:Integer;Matrix:Mat;var Counters: CN );

implementation

procedure SearchInclusions(Width:Integer;Height:Integer;Matrix:Mat;var Counters: CN);

var
  I, J,K: integer;
  Numbers: A21.TIntMassiv;
begin
	for I:=1 to Height do
	begin
		for J := 1 to Width do
		begin
			Setlength(Numbers,0);
			ConvertNumToFig(Matrix[I][J],Numbers);
			for K := 0 to Length(Numbers)-1 do
			begin

				if Numbers[k]<>0 then
					Counters[Numbers[k]]:=Counters[Numbers[k]]+1
				else
					Counters[10]:=Counters[10]+1
			end;								
		end;
	end;
	
end;
end.
