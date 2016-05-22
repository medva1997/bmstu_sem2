program directives;

uses
  Classes
  { you can add units after this };

const
  N_MAX = 5;

type
  TIArray = array [1..N_MAX] of integer;

var
  F : text;
  Arr : TIArray;
  I : integer;
  A : Byte;

begin
  //
  // $I ($IOCHECKS)
  //

  Assign(F, 'test.txt');
  {$I-}
  Reset(F);
  {$I+}
  if IOResult = 0 then
    WriteLn('File exists.')
  else
    WriteLn('File does not exist');

  //
  // $R ($RANGECHECKS)
  //

  for I := 1 to N_MAX + 1 do
    WriteLn('Arr[', I, '] = ', Arr[i]);

  //
  // $Q ($OVERFLOWCHECKS)
  //

  A := 255;
  Inc(A);
  WriteLn('A = ', A);

  ReadLn;
end.

