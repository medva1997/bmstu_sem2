uses crt,sysutils,Classes, rkunits;
var
	WordsList:rkunits.DinStrArray;
	WordsListans1:array [1..4] of string=('Ежик','шел','в','тумане');
	line:String;
	i:Integer;
	flag:Boolean;

begin
	SetLength(WordsList,0);
	
	flag:=false;		
	line:='Ежик шел в тумане';

	BreakLine(line,WordsList);


	for i := 0 to Length( WordsList)-1 do
	begin		
		if(WordsList[i]<>WordsListans1[i+1]) then 	flag:=true; 
		
	end;

	
	if flag=true then writeln('Test1 error')
	else writeln('Test1 pass');

	SetLength(WordsList,0);
	
	
	flag:=false;		
	line:='Ежик шел     в тмане';

	BreakLine(line,WordsList);


	for i := 0 to Length( WordsList)-1 do
	begin		
		if(WordsList[i]<>WordsListans1[i+1]) then flag:=true; 
		
	end;
	
	if flag=true then writeln('Test2 error')
	else writeln('Test2 pass');

end.