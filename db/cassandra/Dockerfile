FROM redhat/ubi9

USER root:root

RUN yum install -y python-pip iputils && \
  pip3 install cassandra-driver && \
  mkdir -p /usr/local/cassandra-app/src
  
COPY src /usr/local/cassandra-app/src

WORKDIR /usr/local/cassandra-app/src

CMD ["sleep", "10000"]

