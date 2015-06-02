all:
	mkdir -p target
	PYTHONPATH=../pypy python ../pypy/rpython/bin/rpython -O 0 --gc=none --output target/rila rila/main.py

install:
	cp target/rila /usr/local/bin/rila

clean:
	rm -rf target/
	rm /usr/local/bin/rila
