FROM ubuntu:16.04

WORKDIR /

RUN apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y wget vim bzip2

RUN apt-get install g++ -y

RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
	bash ~/miniconda.sh -b -p /opt/conda && \
	rm ~/miniconda.sh

ENV PATH /opt/conda/bin:$PATH

RUN conda update conda -y