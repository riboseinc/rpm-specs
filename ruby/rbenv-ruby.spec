%define _prefix /opt/ruby_2.3.4

Name:		rbenv-ruby_2.3.4
Version:	58214
Release: 	2%{?dist:%{dist}}
Group: 		Development/Languages
Summary: 	A ruby instance that can co-exist with other instances in the rbenv (RPM) ecosystem.
License: 	MIT
Source0: 	ruby-2.3.4.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires: 	redhat-rpm-config readline libyaml libyaml-devel readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make libffi-devel openssl-devel
Requires: 	libyaml openssl rbenv

%description
Installs Ruby in a location that rbenv (from RPM) can manage, thereby allowing several version to co-exist. Used https://github.com/imeyer/ruby-1.9.3-rpm SPEC file as guide.

%prep
%setup -n ruby-2.3.4

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"
%configure \
  --disable-rpath 

make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT
# delete source, doc and debug (all in usr dir which we don't want to install)
rm -rf $RPM_BUILD_ROOT/usr
# setup symbolic link and global version for users
%define system_profile_directory $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
install -m 0755 -d %{system_profile_directory}
%define profile_rbenv_ruby_script_filename %{system_profile_directory}/%{name}.sh
cat > %{profile_rbenv_ruby_script_filename} <<END_OF_RBENV_RUBY_PROFILE
# add rbenv ruby path symlink
if [ ! -h ~/.rbenv/versions/2.3.4 ] 
  then
    ln -s %{_prefix} ~/.rbenv/versions/2.3.4
    eval "$(rbenv rehash)"
fi
# add global ruby version if needed.
if [ ! -e ~/.rbenv/version ]
  then
    echo "2.3.4" > ~/.rbenv/version
fi
END_OF_RBENV_RUBY_PROFILE
chmod a+x %{profile_rbenv_ruby_script_filename}

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo " "
echo "rbenv enabled Ruby has been installed in /opt/rbenv-ruby_2.3.4. Log in again to activate."

%files
%dir %{_prefix}
%{_prefix}/*
%{_sysconfdir}/profile.d
%{_sysconfdir}/profile.d/rbenv-ruby_2.3.4.sh

%changelog
* Sun May 07 2017 Aaron Smith <ajsmith10381@gmail.com> - 2.3.4
- Updating to use 2.3.4

* Mon Mar 31 2014 Guy Gershoni <guy@conchus.com> - p76-2
Making /etc/profile.d/rbenv-ruby_2.1.1.sh executable by all so works in RHEL 5

* Mon Mar 24 2014 Guy Gershoni <guy@conchus.com> - 1-0.2.1.1
- Initial version of the package
