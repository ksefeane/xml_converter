FROM alpine
RUN apk update && apk add bash python3
COPY * /
VOLUME ./CSV
VOLUME ./XML
CMD sh autorun
