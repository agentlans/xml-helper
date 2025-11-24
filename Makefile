.PHONY: install uninstall clean

install:
	pip3 install . -r requirements.txt

uninstall:
	pip3 uninstall xml-helper

clean:
	rm -r build xml_helper.egg-info
