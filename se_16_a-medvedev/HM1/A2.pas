{$INCLUDE directive.txt}
{	Search inclusions of digits
	@author(Medvedev Alexey)
	@lastmod(2016/05/13 22:04:00)	
}
unit A2;

interface

uses
  Classes, SysUtils,A21;
type
{ 
	Matrix 100x100 of integer
}
	Mat=array[1..100] of array[1..100] of Integer;
{ 
	Integer array with 10 length
}
	CN=array[1..10] of Integer;

{
	Call procedure as SearchInclusions(10;10;Matrix;Counters);
 @param(Width  Integer, width of matrix)
 @param(Height  Integer, height of matrix)
 @param(Matrix  Array 100x100 of integer where saved user matrix)
 @param(Counters  Array with 10 length where need to save number of inclusions)

}
procedure SearchInclusions(Width:Integer;Height:Integer;Matrix:Mat;var Counters: CN );

implementation

procedure SearchInclusions(Width:Integer;Height:Integer;Matrix:Mat;var Counters: CN);

var
  I, J,K,Len: integer;
  Numbers: A21.TIntMassiv;
begin
	Assert(Height>0);
	Assert(Width> 0);

	for I:=1 to Height do
	begin
		for J := 1 to Width do
		begin
			Setlength(Numbers,0);
			
			ConvertNumToFig(Matrix[I][J],Numbers);

			Len := length(Numbers);
			Assert(Len <> 0);

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
