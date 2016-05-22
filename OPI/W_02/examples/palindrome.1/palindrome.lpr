program palindrome;

uses
  Classes, str_utils
  { you can add units after this };

var
  Word : string;

begin
  Write('Input word: ');
  ReadLn(Word);

  if (length(Word) <> 0) then
    WriteLn('IsNumber(', Word, ') -> ', IsNumber(Word))
  else
    WriteLn('Word is empty');

  ReadLn;
end.

