greeting.exe : hello.o buy.o main.o
	gcc -o greeting.exe hello.o buy.o main.o

test_greeting.exe : hello.o buy.o test.o
	gcc -o test_greeting.exe hello.o buy.o test.o

hello.o : hello.c hello.h
	gcc -std=c99 -Wall -Werror -pedantic -c hello.c

buy.o : buy.c buy.h
	gcc -std=c99 -Wall -Werror -pedantic -c buy.c

main.o : main.c hello.h buy.h
	gcc -std=c99 -Wall -Werror -pedantic -c main.c

test.o : test.c hello.h buy.h
	gcc -std=c99 -Wall -Werror -pedantic -c test.c

clean :
	rm *.o *.exe
