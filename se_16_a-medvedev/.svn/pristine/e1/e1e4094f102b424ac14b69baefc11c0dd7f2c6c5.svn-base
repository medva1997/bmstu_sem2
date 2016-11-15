program main;

{$mode objfpc}{$H+}

uses
  Classes, IArray
  { you can add units after this };

procedure Test1(var Arr : TIArray; var N : integer);
begin
  N := 5;

  Arr[1] := 5;
  Arr[2] := 3;
  Arr[3] := 2;
  Arr[4] := 5;
  Arr[5] := 1;
end;

procedure Test2(var Arr : TIArray; var N : integer);
begin
  N := 5;

  Arr[1] := 5;
  Arr[2] := 3;
  Arr[3] := 2;
  Arr[4] := 5;
  Arr[5] := 6;
end;

var
  Arr : TIArray;
  N : integer;

begin
  Test1(Arr, N);
  writeln('Maximal value is found ', GetMaxCount(Arr, N), ' times.');
  Test2(Arr, N);
  writeln('Maximal value is found ', GetMaxCount(Arr, N), ' times.');
  readln;
end.

