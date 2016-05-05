
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
	while M>1 do
	begin
		SetLength(Numbers,i+1);
		inc(i);
		Numbers[i-1]:=M mod 10;
		M:=M div 10;
	end;
	
end;

end.