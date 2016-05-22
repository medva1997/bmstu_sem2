/// Main module.
/// \author Igor

program palindrome;

{$APPTYPE CONSOLE}

uses
  SysUtils,
  str_utils in 'str_utils.pas';

var
  Word : string;

begin
  Write('Input word: ');
  ReadLn(Word);

  WriteLn('IsNumber(', Word, ') -> ', IsNumber(Word));

  ReadLn;
end.


