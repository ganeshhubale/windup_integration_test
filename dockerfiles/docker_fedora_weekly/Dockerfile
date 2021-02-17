FROM fedora:31

MAINTAINER Shveta Sachdeva <sshveta@redhat.com>
LABEL description="Migration Toolkit for Applications Web-Console"


RUN dnf -y update && dnf clean all
RUN dnf -y install java java-devel unzip wget xterm python3-virtualenv && dnf clean all

# set java env
ENV JAVA_HOME /usr/lib/jvm/java-openjdk
ENV BASE_URL="https://oss.sonatype.org/content/repositories/snapshots/org/jboss/windup"
ENV WEB_CONSOLE="mta-web-distribution"

# Provide snapshot build value
ENV SNAPSHOT_BUILD=snapshot_build
ENV VERSION=build_version

ENV WEB_DISTRIBUTION="${WEB_CONSOLE}/${VERSION}-SNAPSHOT"
ENV WEB_CONSOLE_FILE_PATH="${BASE_URL}/web/${WEB_DISTRIBUTION}/${SNAPSHOT_BUILD}"


RUN echo $WEB_CONSOLE_FILE_PATH

RUN wget -o - $WEB_CONSOLE_FILE_PATH -P /tmp| wc -l > /number && unzip -o /tmp/$SNAPSHOT_BUILD -d /tmp

RUN useradd jboss \
        && usermod -G jboss jboss \
        && mkdir /opt/mta \
        && mkdir /opt/submitted-ears \
        && mkdir /opt/mta-data

WORKDIR /opt/mta

ENV FILE="${WEB_CONSOLE}-${VERSION}-SNAPSHOT"
RUN mv /tmp/${FILE}/* ./ && chown jboss:jboss /opt -R

# For some reason this dir is not empty on docker image and build fails
# TODO investigate and remove this
RUN rm -rf /opt/mta/standalone/configuration/standalone_xml_history/current/*

EXPOSE 8080

USER jboss

ENTRYPOINT ["/opt/mta/run_mta.sh", "-b 0.0.0.0", "-Dwindup.data.dir=/opt/mta-h2-data"]