FLAGS := -std=c99 -Wall -Werror -pedantic

ifeq ($(mode), debug)
FLAGS += -g3 -gdwarf-2
endif

ifeq ($(mode), release)
FLASg += -DNDEBUG -g0
endif

main: main.o  functions.o
	gcc -o $@ $^

tester: functions.o test.o
	gcc -o $@ $^
	
%.o: %.c *.h
	gcc $(FLAGS) -c $<

test:
	./main 
	./main not_exist_file
	./main test1
	./main test2
	./main test3
	./main test4
	./main test5

gcov: 
	rm *.gc*
	c99 -Wall -Werror -pedantic -O0 -fprofile-arcs -ftest-coverage main.c functions.c -o main
	make -B -i test
	gcov main.c functions.c
clean:
	rm *.o
	rm main
	rm tester
	rm *.gc*
