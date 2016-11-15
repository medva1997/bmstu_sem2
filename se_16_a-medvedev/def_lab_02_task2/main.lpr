program main;

{$mode objfpc}{$H+}

uses
  Classes, iarray
  { you can add units after this };

procedure Test1(var Arr : TIArray; var N : integer);
begin
  N := 5;

  Arr[1] := 1;
  Arr[2] := 2;
  Arr[3] := 3;
  Arr[4] := -5;
  Arr[5] := -6;
end;

procedure Test2(var Arr : TIArray; var N : integer);
begin
  N := 5;

  Arr[1] := 1;
  Arr[2] := -2;
  Arr[3] := 3;
  Arr[4] := -5;
  Arr[5] := -6;
end;

var
  Arr, NewArr : TIArray;
  N, NewN : integer;
begin
  Test1(Arr, N);
  Test2(Arr, N);

  FormNewArray(Arr, N, NewArr, NewN);
  PrintArray(NewArr, NewN);

  readln;
end.

