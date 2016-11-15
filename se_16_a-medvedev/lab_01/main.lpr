program main;

{$mode objfpc}{$H+}

uses
  Classes, iarray
  { you can add units after this };

procedure Test1(var Arr : TIArray; var N : integer);
begin
  N := 4;

  Arr[1] := 0;
  Arr[2] := 5;
  Arr[3] := 3;
  Arr[4] := 8;
end;

procedure Test2(var Arr : TIArray; var N : integer);
begin
  N := 4;

  Arr[1] := 9;
  Arr[2] := 5;
  Arr[3] := 3;
  Arr[4] := 8;
end;

var
  Arr : TIArray;
  N   : integer;

begin
  Test1(Arr, N);
  Test2(Arr, N);

  PrintArray(Arr, N);
  writeln('Max pos = ', GetMaxPos(Arr, N));

  readln;
end.

