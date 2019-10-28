FROM conda/miniconda3

COPY mlopsPipelines/AzureMLDocker/requirements.txt  /setup/
	
RUN apt-get update && apt-get install gcc -y

RUN apt-get install g++ -y

RUN pip install --upgrade -r /setup/requirements.txt

CMD ["python"]