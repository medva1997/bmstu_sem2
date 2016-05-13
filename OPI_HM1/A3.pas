{$INCLUDE directive.txt}
{	Search the maximum number of inclusions
	@author(Medvedev Alexey)
	@lastmod(2016/05/13 22:25:00)	
}
unit A3;

interface

uses
  Classes, SysUtils;
type
{ 
	Integer array with 10 length
}
	CN=array[1..10] of Integer;

{
 Search the maximum number of inclusions.Call function as SearchMax(Counters)
 @param(Counters  Array with 10 length where was saved number of inclusions)
 @return(SearchMax Integer, value of most popular digit)
}
function SearchMax(Counters: CN ):Integer;

implementation

function SearchMax(Counters: CN):Integer;
var
  idmax,i: integer;
begin
	idmax:=1;
	for I:=1 to 10 do
	begin
		if Counters[i]>Counters[idmax] then
		begin
			idmax:=i;
		end;
	end;

	if idmax=10 then
	begin
		idmax:=0;			
	end;

	SearchMax:=idmax;
	
end;
end.