FLAGS := -std=c99 -Wall -Werror -pedantic

ifeq ($(mode), debug)
FLAGS += -g3 -gdwarf-2
endif

ifeq ($(mode), release)
FLASg += -DNDEBUG -g0
endif

main: main.o  functions.o
	gcc -o $@ $^

%.o: %.c *.h
	gcc $(FLAGS) -c $<

test:
	./main 
	./main test2
	./main test3
	./main test4
	./main test5
	./main test1
gcov: 
	c99 -Wall -Werror -pedantic -O0 -fprofile-arcs -ftest-coverage main.c functions.c -o main
	make -B -i test
	gcov main.c functions.c
clean:
	rm *.o main test
