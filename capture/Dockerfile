FROM docker.io/rockylinux/rockylinux:9.2

WORKDIR /tmp
RUN dnf install 'dnf-command(config-manager)' -y && dnf install 'dnf-command(reposync)' 
RUN mv /etc/yum.repos.d/* /tmp
ADD https://repository.veeam.com/rocky/9.2/vbr/13.0/mandatory/x86_64/veeam-backup-repo-13.0.0.4967-1.x86_64.rpm veeam-repo.rpm
RUN dnf install -y ./veeam-repo.rpm  && dnf update -y --allowerasing


VOLUME /mirror
WORKDIR /mirror
ENTRYPOINT ["dnf", "reposync", "--download-metadata", "-p", "/mirror"]
