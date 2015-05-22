all:
	mkdir -p target
	PYTHONPATH=../pypy python ../pypy/rpython/bin/rpython --output target/rila rila/main.py

install:
	cp target/rila /usr/local/bin/rila

clean:
	rm -rf target/
	rm /usr/local/bin/rila
