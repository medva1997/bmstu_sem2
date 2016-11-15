unit IArray;

{$mode delphi}

interface

const
  N_MAX = 100;

type
  TIArray = array [1..N_MAX] of integer;

function GetMaxPos(const Arr : TIArray; N : integer) : integer;

procedure PrintArray(const Arr : TIArray; N : integer);

implementation

function GetMaxPos(const Arr : TIArray; N : integer) : integer;
var
  Max  : integer;
  I, J : integer;
begin
  Max := Arr[1];
  J:=1;
  for I := 2 to N do
    if Arr[I] > Max then
    begin
      Max := Arr[I];
      J := I;
    end;

  Result := J;
end;

procedure PrintArray(const Arr : TIArray; N : integer);
var
  I : integer;
begin
  for I := 1 to N do
    write(Arr[I], ' ');
  writeln;
end;

end.

