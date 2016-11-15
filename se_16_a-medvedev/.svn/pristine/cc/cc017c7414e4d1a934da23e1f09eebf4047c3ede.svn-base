
unit rkunits;

interface

uses
  Classes, SysUtils;
type
	{
	Динамический массив строк
	}
	DinStrArray=array of String;
	{
	Динамический массив челых чисел
	}
	DinIntArray=array of Integer;

{
	Разбить строку на слова
	@param(line string, строка со словами)
	@param(WordsList DinStrArray, Список слов)
}
procedure BreakLine(line:String;var WordsList:DinStrArray);
{
	Определение длин слов
	@param(WordsList DinStrArray, Список слов)
	@param(LenList DinIntArray, Список длин слов)
}
procedure CountLenWords(WordsList:DinStrArray; var LenList:DinIntArray);
{
	Определение средней длинны
	@param(LenList DinIntArray, Список длин слов)
}
function SearchMedium(LenList:DinIntArray):real;

implementation

procedure BreakLine(line:String;var WordsList:DinStrArray);
var nline,Word:String;
	i:Integer;
begin
	nline:=line+' ';
	Word:='';

	for i:=1 to Length(nline)do
	begin
		if (' '<>nline[i]) then 
		begin
			Word:=Word+nline[i];
			//writeln(Word);
		end
		else
			begin
				//writeln('qqqq ',Word);
				if Length(Word)>0 then
				begin
					SetLength(WordsList,Length(WordsList)+1);

					WordsList[Length(WordsList)-1]:=Word;
					Word:='';
				end;
			end;
	end;

		
end;


procedure CountLenWords(WordsList:DinStrArray; var LenList:DinIntArray);
var
	I: Integer;
begin
	SetLength(LenList,Length(WordsList));
	for i:=0 to Length(WordsList) do 
	begin
	LenList[i]:=Length(WordsList[i])div 2;	
	//writeln(WordsList[i], ' ', LenList[i]);

	end;
end;


function SearchMedium(LenList:DinIntArray):Real;
var
	i,summ:Integer;
	medium:real;
begin
	summ:=0;
	for i:=0 to Length(LenList)-1 do summ:=LenList[i]+summ;
	medium:=summ/Length(LenList);
	SearchMedium:=medium;
	//writeln(summ,medium);
end;
end.


