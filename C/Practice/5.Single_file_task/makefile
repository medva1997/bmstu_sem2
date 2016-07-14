FLAGS := -std=c99 -Wall -Werror -pedantic

ifeq ($(mode), debug)
FLAGS += -g3 -gdwarf-2
endif

ifeq ($(mode), release)
FLASg += -DNDEBUG -g0
endif

main: main.o  
	gcc -o $@ $^

%.o: %.c 
	gcc $(FLAGS) -c $<

test:
	./main <test1
	./main <test2
	./main <test3
	./main <test4
	./main <test5
	./main <test6
gcov: 
	rm *.gc*
	c99 -Wall -Werror -pedantic -O0 -fprofile-arcs -ftest-coverage *.c -o main
	make -B test
	gcov *.c
clean:
	rm *.o main
	rm *.gc*
