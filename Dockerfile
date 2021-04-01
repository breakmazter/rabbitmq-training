# read about difference between alpine and slim images and figure out which case is yours
FROM python:3.9-alpine

# you can remove redundant ending slash 
COPY consumer.py /work/
# you can use "COPY settings.py ." where . mean current location. (use after setting workdir)
# you can also use "COPY settings.py /work/settings.py" to explicitly demonstrate initial and final location
COPY settings.py /work/

# use "--no-cache-dir -r" This flag will help you avoid loading unnecessary files to image while pip installing libs
# (by default it loads libs archives to install later and caches them to avoid loading again. But in case of docker usage we don't need it) )

# you should update pip before usig as sometimes you can face problems installing libs
RUN pip install requirements.txt

# it's better to move this command to the top as it's usually static and does not change. so you'll avoid creating new layer after having changes in previous layer 
WORKDIR /work/

CMD ["python", "consumer.py"]
