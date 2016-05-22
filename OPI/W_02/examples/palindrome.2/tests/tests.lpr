program tests;

uses
  Classes, str_utils
  { you can add units after this };

procedure Test_IsNumber;
var
  N : integer;
begin
  N := 0;

  if IsNumber('5') <> true then
    inc(N);
  if IsNumber('123') <> true then
    inc(N);
  if IsNumber('77') <> true then
    inc(N);

  if IsNumber('A') <> false then
    inc(N);
  if IsNumber('qwerty') <> false then
    inc(N);
  if IsNumber('12a3') <> false then
    inc(N);
  if IsNumber('d8') <> false then
    inc(N);
  if IsNumber('345x') <> false then
    inc(N);
  if IsNumber('-57') <> false then
    inc(N);
  if IsNumber('+98765') <> false then
    inc(N);
  if IsNumber('') <> false then
    inc(N);

  if (N <> 0) then
    WriteLn('Test_IsNumber FAILED')
  else
    WriteLn('Test_IsNumber OK');
end;


begin
  Test_IsNumber;

  ReadLn;
end.

