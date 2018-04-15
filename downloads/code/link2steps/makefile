SUBDIRS = component_a component_b os
TARGET = hello

all:${SUBDIRS}
	gcc ./obj/*.o -o ${TARGET}

.PHONY: subdirs $(SUBDIRS)  
subdirs: $(SUBDIRS)  
$(SUBDIRS):  
	$(MAKE) -C $@  
	

clean:  
	rm -f ${TARGET}
	rm -rf ./obj/*.*

