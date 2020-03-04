FROM alpine
RUN apk update && apk add bash python3
COPY * /
VOLUME ./CSV
RUN touch /A
CMD sh autorun.sh
