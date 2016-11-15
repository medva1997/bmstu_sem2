{$INCLUDE directive.txt}
{	Convert number to arrray of digits
	@author(Medvedev Alexey)
	@lastmod(2016/05/13 22:06:00)	
}
unit A21;

interface

uses
  Classes, SysUtils;

type
{ 
	Dinamic array of integer
}
	TIntMassiv = array of Integer;

{
 Convert number to arrray of digits. Call procedure as ConvertNumToFig(-67,dinamic_int_array)
 @param(M  Integer number)
 @param(Numbers  Array of integer for save digits of number)
}
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