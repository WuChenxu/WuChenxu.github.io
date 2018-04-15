CC      = gcc  
CFLAGS  = -Wall  
LDFLAGS = -lm  
INCLUDES= -I/usr/local/include

TARGET = os
OBJECTS = main.o

all: ${OBJECTS}
	ld -r -exported_symbols_list exported_sym.list ${OBJECTS}  -o ${TARGET}.o
	mv ${TARGET}.o ../obj/
	rm -rf *.o

%.o : %.c
	${CC} ${CFLAGS} ${INCLUDES} -c $< -o $@

clean:
	rm -rf *.o

