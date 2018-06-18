# Original from https://github.com/remicollet/remirepo/blob/master/mydumper/mydumper.spec

Name:           mydumper
Version:        0.9.5
Release:        1%{?dist}
Summary:        A high-performance MySQL backup tool

Group:          Applications/Databases
License:        GPLv3+
URL:            https://github.com/maxbube/mydumper
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  glib2-devel mysql-devel zlib-devel pcre-devel openssl-devel
BuildRequires:  cmake python-sphinx

%description
Mydumper (aka. MySQL Data Dumper) is a high-performance multi-threaded backup
(and restore) toolset for MySQL and Drizzle.

The main developers originally worked as Support Engineers at MySQL
(one has moved to Facebook and another to SkySQL) and this is how they would
envisage mysqldump based on years of user feedback.

%prep
%setup -q

sed -e 's/-Werror//' -i CMakeLists.txt


%build

# TODO: enable BINLOG later. Enabling now gives error:
# /usr/include/mysql/sql_common.h:26:18: fatal error: hash.h: No such file or directory
# #include <hash.h>

%cmake \
  -DRUN_CPPCHECK=ON \
  -DWITH_BINLOG=OFF

%make_build


%install
%make_install

rm -f %{buildroot}%{_datadir}/doc/%{name}/html/.buildinfo


%files
%defattr(-,root,root,-)
%doc %{_docdir}
%{_bindir}/mydumper
%{_bindir}/myloader
%{_mandir}/man1/mydumper.*
%{_mandir}/man1/myloader.*


%changelog
* Sun Jun 18 2018 Ronald Tse <ronald.tse@ribose.com> - 0.9.5-1
- Version bump to 0.9.5

* Thu May 18 2016 Ronald Tse <ronald.tse@ribose.com> - 0.9.1-2
- Works with CentOS 7.3 and includes docs

* Mon Nov 16 2015 Vicente Dominguez <twitter:@vicendominguez> - 0.9.1
- Ugly and fast rpm for CentOS 6.5

* Mon Sep 29 2014 Vicente Dominguez <twitter:@vicendominguez> - 0.6.2
- Ugly fast rpm for CentOS 6.5

* Fri Feb 28 2014 Vicente Dominguez <twitter:@vicendominguez> - 0.6.1
- Ugly fast rpm for CentOS 6

* Fri Feb 28 2014 Vicente Dominguez <twitter:@vicendominguez> - 0.6.0
- Ugly fast rpm for CentOS 6 but it works

* Thu Jan  3 2013 Remi Collet <remi@fedoraproject.org> - 0.2.3-2
- don't break build because of warnings
  (lot of deprecated glib calls on fedora 18)

* Sun Apr 15 2012 Remi Collet <remi@fedoraproject.org> - 0.2.3-1
- initial package
