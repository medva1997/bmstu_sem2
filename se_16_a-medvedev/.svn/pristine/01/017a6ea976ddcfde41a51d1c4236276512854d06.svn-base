program integral;

{$APPTYPE CONSOLE}

uses
    SysUtils;

type
    TFunction = function(x : real) : real;

function F_1(x : real) : real;
begin
    result := x + 1.0;
end;

function F_2(x : real) : real;
begin
    result := sin(x);
end;

function F_3(x : real) : real;
begin
    result := exp(x);
end;

function Trapezium(A, B : real; N : integer; Func : TFunction) : real;
var
    H : real;
    X, Y : real;
    Sum : real;
    I : integer;
begin
    H := (B - A) / N;

    Sum := 0;
    for I := 0 to N  do
    begin
        X := A + I * H;
        Y := Func(X);

        if i = 0 then
            Sum := Sum + Y / 2.0
        else
            if i = N  then
                Sum := Sum + Y / 2.0
            else
                Sum := Sum + Y;
     end;

     result := Sum * H;
end;

var
    A, B : real;
    N : integer;
    Choise : integer;

begin
    WriteLn('Input a:');
    ReadLn(A);
    WriteLn('Input b:');
    ReadLn(B);

    repeat
        WriteLn('Input n (100 <= n <= 5000):');
        ReadLn(N);
    until (N >= 100) and (N <= 5000);

    repeat
        WriteLn('Input function:');
        WriteLn('0 - x + 1');
        WriteLn('1 - sin(x)');
        WriteLn('2 - exp(x)');
        ReadLn(Choise);
    until (Choise >= 0) and (Choise <= 2);

    case Choise of
        0 : WriteLn('Integral of "x + 1" from ', A:4:2, ' till ', B:4:2, ' = ', Trapezium(A, B, N, F_1):6:2);
        1 : WriteLn('Integral of "sin(x)" from ', A:4:2, ' till ', B:4:2, ' = ', Trapezium(A, B, N, F_2):6:2);
        2 : WriteLn('Integral of "exp(x)" from ', A:4:2, ' till ', B:4:2, ' = ', Trapezium(A, B, N, F_3):6:2);
    end;

    ReadLn;
end.
