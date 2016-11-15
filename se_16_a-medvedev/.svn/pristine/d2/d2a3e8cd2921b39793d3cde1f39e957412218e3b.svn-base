
unit A21;

interface

uses
  Classes, SysUtils;

type TIntMassiv = array of Integer;

Procedure ConvertNumToFig(M:Integer; var Numbers:TIntMassiv);

implementation
procedure ConvertNumToFig(M:Integer; var Numbers:TIntMassiv);
var i:integer;
begin
	i:=0;
	if (M=0) then
	begin
		SetLength(Numbers,1);
		Numbers[0]:=0
	end
	else
		M:=Abs(M);
		while M>0 do
		begin
			SetLength(Numbers,i+1);
			inc(i);
			Numbers[i-1]:=M mod 10;
			M:=M div 10;
		end;
	
end;

end.