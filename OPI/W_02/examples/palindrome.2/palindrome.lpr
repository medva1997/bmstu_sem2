program palindrome;

uses
  Classes, str_utils
  { you can add units after this };

var
  Word : string;

begin
  Write('Input word: ');
  ReadLn(Word);

  WriteLn('IsNumber(', Word, ') -> ', IsNumber(Word));

  ReadLn;
end.

