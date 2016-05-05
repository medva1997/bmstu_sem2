unit A3;

interface

uses
  Classes, SysUtils;
type
	CN=array[1..10] of Integer;

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