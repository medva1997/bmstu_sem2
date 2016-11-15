unit IArray;

{$mode delphi}

interface

const
  N_MAX = 100;

type
  TIArray = array [1..N_MAX] of integer;

function GetMaxCount(const Arr : TIArray; N : integer) : integer;

implementation

function GetMaxCount(const Arr : TIArray; N : integer) : integer;
var
  I : integer;
  Max, Count : integer;
begin
  Max := Arr[1];
  Count := 1;

  for I := 2 to N do
    if Arr[i] > Max then
      begin
        Max := Arr[i];
        Count := 1;
      end
    else
      if Max = Arr[i] then
        Count := Count + 1;

  Result := Count;
end;

end.