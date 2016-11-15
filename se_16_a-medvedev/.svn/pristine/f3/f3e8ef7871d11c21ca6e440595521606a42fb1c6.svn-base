uses crt,sysutils,Classes,A21;

type TIntMassiv = array of Integer;
var
  Numbers: A21.TIntMassiv;
  line:String;

begin
	line:='Test1';
	ConvertNumToFig(0,Numbers);

	if 1<>Numbers[0] then
	begin
		Writeln('Module A21 '+line+' FAILED');
	end
	else
		Writeln('Module A21 '+line+' pass');



	line:='Test2';
	ConvertNumToFig(-1,Numbers);

	if 1<>Numbers[0] then
	begin
		Writeln('Module A21 '+line+' FAILED');
	end
	else
		Writeln('Module A21 '+line+' pass');

	line:='Test3';
	ConvertNumToFig(10,Numbers);

	if (0<>Numbers[0])and (1<>Numbers[1]) then
	begin
		Writeln('Module A21 '+line+' FAILED');
	end
	else
		Writeln('Module A21 '+line+' pass');
end.
