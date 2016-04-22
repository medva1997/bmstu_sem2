uses crt,dateutils,sysutils;
const N3=1000000;
      M=10;

type
    Massiv = array [1 .. N3] of integer;
    Massiv2 =array [1 .. N3] of array[1..M] of integer;
var I,J,N,Z: integer;
    st,fn,timeUp,timeRandom,timeDown:TDateTime;
    A: Massiv;
    B: Massiv2;

procedure ArrayUp(var A: Massiv;  N: integer) ;
begin
  for I := 1 to N do
  A[I]:=I;
end;

procedure ArrayDown(var A: Massiv;  N: integer);
begin
  for I := 1 to N do
    A[I]:=N-I
end ;

procedure ArrayRandom( var A: Massiv;  N: integer);
begin
	randomize;
  for I := 1 to N do
    A[I]:=random(N) ;
end;


procedure ArrayUpInf(var A: Massiv2;  N: integer) ;
begin
  for I := 1 to N do
    for J := 1 to M do
      A[I][J]:=I;
end;

procedure ArrayDownInf(var A: Massiv2;  N: integer);
begin
  for I := 1 to N do
    for J := 1 to M do
      A[I][J]:=N-I
end ;

procedure ArrayRandomInf( var A: Massiv2;  N: integer);
begin
  randomize;
  for I := 1 to N do
    for J := 1 to M do
      A[I][J]:=random(N) ;
end;

procedure Shell(var A: Massiv; N: Integer);
var
  K, T,B: Integer;
  H: array [1 .. 11] of Integer;

begin

  H[1] := 1750;
  H[2] := 701;
  H[3] := 301;
  H[4] := 132;
  H[5] := 57;
  H[6] := 23;
  H[7] := 10;
  H[8] := 4;
  H[9] := 1;

  for T := 1 to 9 do
  begin
    K := H[T];
    for I := K + 1 to N do
    begin

      B := A[I];
      J := I - K;
        while (J > 0) and (B < A[J]) do
        begin
          A[J + K] := A[J];
          J := J - K;
        end;
        A[J + K] := B;
      end;
    end;

end;


procedure ShellInf(var A: Massiv2; N: Integer);
var
  K, T: Integer;
  H: array [1 .. 11] of Integer;
  F: array [1 .. M] of Integer;

begin

  H[1] := 1750;
  H[2] := 701;
  H[3] := 301;
  H[4] := 132;
  H[5] := 57;
  H[6] := 23;
  H[7] := 10;
  H[8] := 4;
  H[9] := 1;

  for T := 1 to 9 do
  begin
    K := H[T];
    for I := K + 1 to N do
    begin

      F := A[I];
      J := I - K;
        while (J > 0) and (F[2]< A[J][2]) do
        begin
          A[J + K] := A[J];
          J := J - K;
        end;
        A[J + K]:= F;
      end;
    end;

end;

procedure Shell1(var A: Massiv; N: Integer);
var
  i, j, step, tmp : Integer;
begin

     step:=N div 2;  // step:=step shr 1
  While step>0 Do Begin
    For i:=step to N Do Begin
      tmp:=A[i];
      j:=i;
      While (j>=step) and (A[j-step]>tmp) Do Begin
        A[j]:=A[j-step];
        dec(j,step);
      End;
      A[j]:=tmp;
    End;
    step:=step div 2;  // step:=step shr 1
  End;

end;




BEGIN
Writeln('Сортировка Шелла');
Writeln('Время указано в мс');
Writeln('N      ','|',' Возрастающий ','|','   Случайный  ','|','Убыв.');
Z:=0;
N:=N3 div 1000;
while Z<3 do
  begin
  N:=N*10;

  //Sort up
  ArrayUp(A,N);
  st:=Now;
  Shell(A, N);
  fn:=Now;
  timeUp:=MillisecondOf(fn-st);

  //Sort random
  ArrayRandom(A,N);
  st:=Now;
  Shell(A, N);
  fn:=Now;
  timeRandom:=MillisecondOf(fn-st);

  //Sort down
  ArrayDown(A,N);
  st:=Now;
  Shell(A, N);
  fn:=Now;
  timeDown:=MillisecondOf(fn-st);

  Writeln(N:7,'|',timeUp:14:0,'|',timeRandom:14:0,'|',timeDown:5:0);
  Z:=Z+1;
  end;

//Sort with information
Z:=0;
N:=N3 div 1000;
Writeln;
Writeln('C доп информацией');

while Z<3 do
  begin
  N:=N*10;
  //Sort up
  ArrayUpInf(B,N);
  st:=Now;
  ShellInf(B, N);
  fn:=Now;
  timeUp:=MillisecondOf(fn-st);

  //Sort random
  ArrayRandomInf(B,N);
  st:=Now;
  ShellInf(B, N);
  fn:=Now;
  timeRandom:=MillisecondOf(fn-st);

  //Sort down
  ArrayDownInf(B,N);
  st:=Now;
  ShellInf(B, N);
  fn:=Now;
  timeDown:=MillisecondOf(fn-st);
  


  Writeln(N:7,'|',timeUp:14:0,'|',timeRandom:14:0,'|',timeDown:5:0);
  Z:=Z+1;
  end;
END.