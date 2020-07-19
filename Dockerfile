FROM alpine
RUN apk add --no-cache build-base libffi-dev openssl-dev openssh unzip zlib-dev
WORKDIR /root
RUN wget https://github.com/brandtbucher/cpython/archive/patma.zip
RUN unzip patma.zip
WORKDIR /root/cpython-patma/
RUN ./configure --enable-optimizations
RUN make
RUN make install
WORKDIR /
RUN rm -r /root/cpython-patma
RUN ln -s /usr/local/bin/python3.10 /usr/local/bin/python
RUN ln -s /usr/local/bin/python3.10-config /usr/local/bin/python-config
CMD ["python"]
