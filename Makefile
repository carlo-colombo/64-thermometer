include makext.mk

help: .help

MPY=../micropython/mpy-cross/build/mpy-cross	

files:=st7789_base.mpy st7789_ext.mpy publish.mpy app.mpy

%.mpy : %.py
	$(MPY) $?
	mpremote cp $? :
	
main.py: $(files) # main.py
	mpremote cp $@ :

upload: main.py # upload 

upload-images: # upload all .565 images
	mpremote cp pngs/*.565 :

clean: # clean
	rm *.mpy

all: upload upload-images#