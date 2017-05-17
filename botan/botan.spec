%global major_version 2
%global reldate 20170517
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           botan
Version:        %{major_version}.1.0
Release:        1%{?dist}
Summary:        Crypto library written in C++

Group:          System Environment/Libraries
License:        BSD
URL:            http://botan.randombit.net/
Source0:	      %{url}/releases/Botan-%{version}.tgz
# tarfile is stripped using repack.sh. original tarfile to be found
# here: http://botan.randombit.net/releases/Botan-%%{version}.tgz
#Source0:        Botan-%{version}.tgz

BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires:  python
BuildRequires:  python-devel
%if 0%{?with_python3}
BuildRequires:  python3
BuildRequires:  python3-devel
%endif # with_python3


%description
Botan is a BSD-licensed cryptographic library written in C++. It provides a
wide variety of basic cryptographic algorithms, X.509 certificates and CRLs,
PKCS \#10 certificate requests, a filter/pipe message processing system, and a
wide variety of other features, all written in portable C++.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       bzip2-devel
Requires:       zlib-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation for %{name}
Group:          Documentation
BuildArch:      noarch
BuildRequires:	doxygen

%description    doc
This package contains HTML documentation for %{name}.


# %package -n python-%{name}
# Summary:        Python bindings for %{name}
# Group:          System Environment/Libraries
# %{?python_provide:%python_provide python2-%{name}}
# # the python2 package was named botan-python up to 1.10.13-1
# Provides:       %{name}-python = %{version}-%{release}
# Obsoletes:      %{name}-python < 1.10.13-2
#
# %description -n python2-%{name}
# %{summary}
#
# This package contains the Python2 binding for %{name}.
#
# Note: The Python binding should be considered alpha software, and the
# interfaces may change in the future.

%prep
# not %{name} here because Botan-x starts with a capital B
%autosetup -n Botan-%{version}
export CXXFLAGS="${CXXFLAGS:-%optflags}"
# (ab)using CXX as an easy way to inject our CXXFLAGS
export CXX="g++ -std=c++11 -pthread ${CXXFLAGS:-%{optflags}}"

%build
./configure.py \
  --prefix=%{_prefix} \
  --bindir=%{_bindir} \
  --libdir=%{_libdir} \
  --includedir=%{_includedir} \
  --docdir=%{_pkgdocdir} \
  --cc=gcc \
  --os=linux \
  --cpu=%{_arch} \
  --with-boost \
  --with-zlib \
  --with-bzip2 \
  --with-python-versions=dummy.dummy \
  --with-doxygen
%make_build

%{_bindir}/doxygen build/botan.doxy

%install
%make_install

# %{_bindir}/find %{buildroot} -name '*.la' -delete -print
# 
# %{__mkdir} -p %{buildroot}/%{_pkgdocdir}
# %{__cp} -pr doc/html ChangeLog README README.* %{buildroot}/%{_pkgdocdir}
# %{_sbindir}/hardlink -cvf %{buildroot}/%{_pkgdocdir}

# TODO: Install Python binding from "src/python/botan2.py"

# TODO: Install documentation properly for Botan 2
# fixups
# find doc/examples -type f -exec chmod -x {} \;
# mv doc/examples/python doc/python2-examples
# cp -a doc/{examples,python2-examples,license.txt} \
#    %{buildroot}%{_pkgdocdir}
# cp -a %{SOURCE1} %{buildroot}%{_pkgdocdir}
# rm -r %{buildroot}%{_pkgdocdir}/manual/{.doctrees,.buildinfo}


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


# TODO: Install files properly for Botan 2
%files
%doc %dir %{_pkgdocdir}
%license %{_pkgdocdir}/license.txt
%{_bindir}/botan
%{_libdir}/lib%{name}-%{major_version}.so.*
%{_libdir}/python*/site-packages/botan2.py


# TODO: Install files properly for Botan 2
%files devel
%doc %{_pkgdocdir}/doxygen
%{_includedir}/%{name}/
%exclude %{_libdir}/libbotan-%{major_version}.a
%{_libdir}/libbotan-%{major_version}.so
%{_libdir}/pkgconfig/botan-%{major_version}.pc
# %{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-%{major_version}.so
%{_libdir}/pkgconfig/%{name}.pc


# TODO: Install files properly for Botan 2
%files doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/manual
# next files duplicated on purpose, because -doc doesn't depend on the
# main package
# %{_pkgdocdir}/readme.txt
%license %{_pkgdocdir}/license.txt

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./botan-test


%changelog
* Tue May 16 2017 Ribose Packaging <packaging@ribose.com> - 2.1.0-1
- Upgrade to 2.1.0

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.10.14-5
- Rebuilt for Boost 1.63

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.10.14-4
- Rebuild for Python 3.6

* Sat Dec 10 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.14-3
- Add -std=c++11 to the compilerflags (needed on EPEL7).

* Fri Dec  9 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.14-2
- Update to 1.10.14.
- Depend on OpenSSL 1.0 compat package for F26+.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.13-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jul  3 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.13-3
- Fix typo.

* Sun Jul  3 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.13-2
- Provide python2- and python3- subpackages (rhbz#1313786).
- Move python examples to -doc subpackage.

* Fri Apr 29 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.13-1
- Update to 1.10.13.

* Mon Feb  8 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.12-1
- Update to 1.10.12.
- Mark license.txt with %%license.
- Change %%define -> %%global.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 1.10.9-9
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.10.9-8
- Rebuilt for Boost 1.59

* Fri Jul 24 2015 David Tardon <dtardon@redhat.com> - 1.10.9-7
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.9-5
- Rebuild for gcc5.

* Fri Feb  6 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.9-4
- Re-enable cleared ECC. Patch by Tom Callaway <spot@fedoraproject.org>.

* Thu Feb  5 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.9-3
- Disable gmp engine (see bug 1116406).
- Use _pkgdocdir.

* Thu Feb  5 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.9-2
- Remove workaround for bug 1186014.

* Sat Jan 31 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.9-1
- Update to 1.10.9.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 Björn Esser <bjoern.esser@gmail.com> - 1.10.8-5
- rebuild for boost 1.55.0 (libboost_python.so.1.55.0)

* Sun May 25 2014 Brent Baude <baude@us.ibm.com> - 1.10.8-4
- Added ppc64le arch support

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 1.10.8-3
- rebuild for boost 1.55.0

* Mon May 12 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1.10.8-2
- Added AArch64 architecture support

* Sat May 10 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.8-1
- Update to 1.10.8.

* Tue Sep  3 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.5-4
- Re-enable IDEA (rhbz#1003052) and SRP-6.

* Sat Jul 27 2013 Petr Machata <pmachata@redhat.com> - 1.10.5-3
- Rebuild for boost 1.54.0

* Fri Jul 26 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.5-2
- Rename the subpackage for the Python binding.

* Fri Jul 26 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.10.5-1
- Update to 1.10.5.
- Modernize spec file.
- New -doc subpackage containing HTML documentation.
- Package Python binding.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 25 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.14-1
- Update to 1.8.14.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.13-5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.13-4.2
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.13-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.8.13-2.2
- rebuild with new gmp without compat lib

* Mon Oct 10 2011 Peter Schiffer <pschiffe@redhat.com> - 1.8.13-2.1
- rebuild with new gmp

* Thu Jul 21 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.13-2
- Patch to revert the soname change.

* Wed Jul 20 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.13-1
- Update to 1.8.13.

* Sat Jul  2 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.12-1
- Update to 1.8.12.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov  6 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.11-1
- Update to 1.8.11.

* Sat Sep  4 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.10-1
- Update to 1.8.10.

* Sun Aug 29 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.9-4
- Update README.fedora.

* Fri Aug 27 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.9-3
- Also remove RC5 from the tarfile.
- Comment out RC5, RC6 and IDEA validation tests.

* Wed Aug  4 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.9-2
- Remove IDEA, RC6, and ECC-related modules from the tarfile,
  see bz 615372.

* Wed Jun 16 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.9-1
- Update to 1.8.9.
- Drop patch applied upstream.

* Thu Nov 19 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.8-2
- Add patch from upstream to build with binutils-2.20.51.0.2.
  Fixes bz 538949 (ftbfs).

* Thu Nov  5 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.8-1
- Update to 1.8.8, a bugfix release.

* Thu Sep 10 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.7-1
- Update to 1.8.7. This is mainly a bugfix release.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.8.6-2
- rebuilt with new openssl

* Thu Aug 13 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.6-1
- Update to 1.8.6, which contains new features as well as bugfixes,
  e.g. concerning the /proc-walking entropy source.

* Wed Aug 12 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.5-2
- Fix changelog.

* Wed Aug 12 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.5-1
- Update to 1.8.5.
- Use .tbz source file.
- Configuration script uses python now.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 25 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.2-1
- Update to 1.8.2.

* Mon Mar 16 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.1-4
- Add missing requirements to -devel package.

* Fri Feb 27 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.1-3
- Rebuilt again after failed attempt in mass rebuild.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.1-1
- Update to 1.8.1. This is a bugfix release, see
  http://botan.randombit.net/news/releases/1_8_1.html for changes.
- No need to explicitly enable modules that will be enabled by
  configure.pl anyway.

* Mon Jan 19 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.0-2
- Move api* and tutorial* doc files to -devel package.

* Sat Jan 17 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.8.0-1
- New package.
