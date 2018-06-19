# PDF Generator for OBS

#### NOTE: Python 3 Only

### Image source

Unzip into /opt/obs/images

https://cdn.unfoldingword.org/obs/jpg/obs-images-360px.zip
https://unfoldingword.org/assets/img/uW-Level-1-128px.png
https://unfoldingword.org/assets/img/uW-Level-2-128px.png
https://unfoldingword.org/assets/img/uW-Level-3-128px.png
https://cdn.door43.org/obs/jpg/uWOBSverticallogo1200w.png
https://cdn.door43.org/obs/jpg/uWOBSverticallogo600w.png

### To run in Python 3.6
```bash
cd /opt && git clone https://github.com/unfoldingWord-dev/obs-pdf.git
cd /opt/obs-pdf && pip3 install -r requirements.txt
cd /opt/obs-pdf && python3 -m app.pdf_from_dcs --lang-code=en
```

### Docker commands
```bash
docker run --name dcs-context -d --rm --workdir /opt -i -t dcs-context
docker exec dcs-context git clone https://github.com/unfoldingWord-dev/obs-pdf.git
docker exec -i dcs-context bash -c "cd /opt/obs-pdf && git fetch --all && git checkout origin/develop"
docker exec -i dcs-context bash -c "cd /opt/obs-pdf && pip3 install -r requirements.txt"
docker exec -i dcs-context bash -c "cd /opt/obs-pdf && python3 -m app.pdf_from_dcs --lang-code=en"
docker cp dcs-context:/opt/obs-pdf/output /home/phil/docker-output
docker stop dcs-context
```
