{$INCLUDE directive.txt}
uses crt,sysutils,Classes, rkunits;
var filein,fileout,line:String;
	tin,tout:text;
	WordsList:rkunits.DinStrArray;
	LenList:rkunits.DinIntArray;
	linemedium: Real;

begin
	writeln('Введите имя входного файла: ');
	Readln(filein);	
	//filein:='/home/alexey/repos/se_16_a-medvedev/PK2/in1.txt';
	assert(FileExists(filein),'not found file');

	assign(tin,filein);
  	reset(tin);
	
	writeln('Введите имя файла для вывода результа: ');
	Readln(fileout);
	//fileout:='/home/alexey/repos/se_16_a-medvedev/PK2/out2.txt';
	
	assign(tout,fileout);
  	rewrite(tout);

	while not eof(tin) do
	begin

		SetLength(WordsList,0);
		SetLength(LenList,0);
		linemedium:=0;		
		readln(tin,line);

		BreakLine(line,WordsList);
		CountLenWords(WordsList,LenList);
		linemedium:=SearchMedium(LenList);
		//writeln(linemedium:5:3);
		writeln(tout,linemedium:5:3);

	end;
	close(tin);
	close(tout);
end.