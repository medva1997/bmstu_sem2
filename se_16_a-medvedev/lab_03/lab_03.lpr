program integral;

{$APPTYPE CONSOLE}

uses
  SysUtils;


type
  TIArray = array [1..100] of integer;

procedure Test1(var a : TIArray; var n : integer);
begin
  n := 10;

  a[1] := 1;
  a[2] := 2;
  a[3] := 3;
  a[4] := 4;
  a[5] := 5;
  a[6] := 6;
  a[7] := 7;
  a[8] := 8;
  a[9] := 9;
  a[10] := 10;
end;

procedure Change(var a : TIArray; var n : integer);
var
 i,y:integer;
begin
  i:=1;  
  while i <= n do
  begin
    if i <= n div 2 then
    begin
      y:=a[n-i+1];
      a[n-i+1]:=a[i];
      a[i]:= y;
    end;
  i := i + 1;
  end;


end;



procedure PrintArray(const a : TIArray; n : integer);
var
  I : integer;
begin
  for I := 1 to n do
    write(a[I], ' ');
  writeln;
end;


var
  i, n, x, y : integer;
  a : TIArray;

begin

  Test1(a, n);

  PrintArray(a, n);  
  Change(a,n);

  PrintArray(a, n);  
 
  readln;
end.

