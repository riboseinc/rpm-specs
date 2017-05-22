RPMBUILD_CMD=rpmbuild
RPMBUILD_FLAGS="-v -ba"

yum install -y epel-release
yum install -y openssl openssl-devel expat expat-devel libtool gcc-c++ ncurses-devel openssh tcl-devel tk-devel unixODBC-devel
yum install -y java-1.7.0-openjdk-devel krb5-devel wxGTK-devel

yum install -y automake autoconf libtool hardlink doxygen make \
  rpmdevtools wget epel-rpm-macros

rpmdev-setuptree
cd ~/rpmbuild/SOURCES
# curl -L -O http://www.erlang.org/download/otp_src_R15B01.tar.gz
# curl -L -O http://www.erlang.org/download/otp_doc_html_R15B01.tar.gz
# curl -L -O http://www.erlang.org/download/otp_doc_man_R15B01.tar.gz
curl -L -O http://pkgs.fedoraproject.org/repo/pkgs/erlang/otp_src_R15B01.tar.gz/f12d00f6e62b36ad027d6c0c08905fad/otp_src_R15B01.tar.gz
curl -L -O http://pkgs.fedoraproject.org/repo/pkgs/erlang/otp_doc_html_R15B01.tar.gz/7569cae680eecd64e7e5d952be788ee5/otp_doc_html_R15B01.tar.gz
curl -L -O http://pkgs.fedoraproject.org/repo/pkgs/erlang/otp_doc_man_R15B01.tar.gz/d87412c2a1e6005bbe29dfe642a9ca20/otp_doc_man_R15B01.tar.gz

$ vi erlang-rpmlintrc
echo 'addFilter("erlang.* devel-file-in-non-devel-package")' > erlang-rpmlintrc

cd ~/rpmbuild/SPECS
yes | cp -f /usr/local/erlang/erlang.spec ~/rpmbuild/SPECS
cd ~/rpmbuild/SPECS

QA_RPATHS=$[ 0x0001|0x0010|0x0002 ] rpmbuild ${RPMBUILD_FLAGS} erlang.spec

