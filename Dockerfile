FROM alpine

# basic flask environment
RUN apk add --no-cache bash git nginx uwsgi uwsgi-python3 cmd:pip3 \
	&& pip3 install --upgrade pip \
	&& pip3 install flask


RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

RUN pip3 install mysqlclient

# application folder
ENV APP_DIR /app

# app dir
RUN mkdir ${APP_DIR} \
	&& chown -R nginx:nginx ${APP_DIR} \
	&& chmod 777 /run/ -R \
	&& chmod 777 /root/ -R
VOLUME ${APP_DIR}
WORKDIR ${APP_DIR}

COPY /backend ${APP_DIR}

# # Install requirements
RUN pip install --no-cache-dir -r requirements.txt


#
# expose web server port
# only http, for ssl use reverse proxy
EXPOSE 80

# copy config files into filesystem
COPY nginx.conf /etc/nginx/nginx.conf
COPY app.ini /app.ini
COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]}