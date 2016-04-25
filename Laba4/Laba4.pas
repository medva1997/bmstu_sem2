uses crt,dateutils,sysutils;
const N3=250000;
      M=10;
      cities:array[1..5] of String=('Moscow','NY','London','Miamy','Tokio');
      works:array[1..5] of String=('reporter', 'writer','driver','fireman','policeman');

type
    Data =Record
      city:String;
      number:integer;
      work:String;
      id:integer;
      end;

    Massiv = array [1 .. N3] of integer;
    Massiv2= array [1 .. N3] of Data;

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
var k:integer;
begin
  for I := 1 to N do
   begin
      k:=I;
      A[I].city:=cities[(k mod 5)+1];;
      A[I].number:=k;
      A[I].work:=works[(k mod 5)+1];
      A[I].id:=N-k;     
   end; 
end;

procedure ArrayDownInf(var A: Massiv2;  N: integer);
var k:integer;
begin
  for I := 1 to N do
  begin
      k:=N-I;
      A[I].city:=cities[(k mod 5)+1];;
      A[I].number:=k;
      A[I].work:=works[(k mod 5)+1];
      A[I].id:=N-k;     
   end; 

      
end ;

procedure ArrayRandomInf( var A: Massiv2;  N: integer);
Var k:integer;
begin
  randomize;
  for I := 1 to N do
  begin
      k:=random(N);
      A[I].city:=cities[(k mod 5)+1];;
      A[I].number:=k;
      A[I].work:=works[(k mod 5)+1];
      A[I].id:=N-k;     
   end; 
      

end;

procedure Shell(var A: Massiv; N: Integer);
var
  K, T,B: Integer;
  H: array [1 .. 15] of Integer;

begin
  H[1]:=7174453;
  H[2]:=2391484;
  H[3]:=797161;
  H[4]:=265720;
  H[5]:=88573;
  H[6]:= 29524;
  H[7] := 9841;
  H[8] := 3280;
  H[9] := 1093;
  H[10] := 364;
  H[11] := 121;
  H[12] := 40;
  H[13] := 13;
  H[14] := 4;
  H[15] := 1;
  for T := 1 to 15 do
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
  H: array [1 .. 15] of Integer;
  F: Data;

begin
  H[1]:=7174453;
  H[2]:=2391484;
  H[3]:=797161;
  H[4]:=265720;
  H[5]:=88573;
  H[6]:= 29524;
  H[7] := 9841;
  H[8] := 3280;
  H[9] := 1093;
  H[10] := 364;
  H[11] := 121;
  H[12] := 40;
  H[13] := 13;
  H[14] := 4;
  H[15] := 1;

  for T := 1 to 15 do
  begin
    K := H[T];
    for I := K + 1 to N do
    begin

      F := A[I];
      J := I - K;
        while (J > 0) and (F.number< A[J].number) do
        begin
          A[J + K] := A[J];
          J := J - K;
        end;
        A[J + K]:= F;
      end;
      //riteln(A[10000].city)
    end;

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
  Writeln;
  Writeln('Пример элемента с доп информацией: ');
  Writeln(' Город: ', B[10000].city);
  Writeln(' Номер: ', B[10000].number);
  WriteLN(' Работа: ', B[10000].work);
  Writeln(' id: ', B[10000].id);
END.