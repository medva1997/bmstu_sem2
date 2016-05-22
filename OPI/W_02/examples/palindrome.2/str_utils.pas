unit str_utils;

interface

uses
  Classes, SysUtils;

function IsNumber(const Word: string) : boolean;

implementation

function IsNumber(const Word: string) : boolean;
var
  I, Len : integer;
  Rc : boolean;
begin
  Len := length(Word);
  if (Len = 0) then
    Rc := false
  else
  begin
    Rc := true;
    I  := 1;
    while (Rc = true) and (I <= Len) do
    begin
      if not(Word[I] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']) then
        Rc := false;
      inc(I);
    end;
  end;

  IsNumber := Rc;
end;


end.

