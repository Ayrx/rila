all:
	mkdir -p target
	PYTHONPATH=../pypy python ../pypy/rpython/bin/rpython --output target/rila rila/main.py

clean:
	rm -rf target/
