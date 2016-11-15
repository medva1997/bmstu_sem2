unit IArray;

{$mode delphi}

interface

const
  N_MAX = 100;

type
  TIArray = array [1..N_MAX] of integer;

procedure FormNewArray(const Arr : TIArray; N : integer;
                            var NewArr : TIArray; var NewN : integer);

procedure PrintArray(const Arr : TIArray; N : integer);

implementation

procedure FormNewArray(const Arr : TIArray; N : integer;
                            var NewArr : TIArray; var NewN : integer);
var
  I : integer;
begin
  NewN := 0;
  for I := 1 to N do
    if Arr[i] > 0 then
    begin
      NewArr[i] := Arr[i];
      NewN := NewN + 1;
    end;
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

