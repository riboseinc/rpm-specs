%global reldate 20160607
%global origname json-c
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}


Name:		json-c12
Version:	0.12.1
Release:	1%{?dist}
Summary:	JSON implementation in C (0.12 compatibility package)

License:	MIT
URL:		https://github.com/%{origname}/%{origname}
Source0:	%{url}/archive/json-c-%{version}-%{reldate}.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool

%description
JSON-C implements a reference counting object model that allows you
to easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C representation
of JSON objects.  It aims to conform to RFC 7159.


%package devel
Summary:	Development files for %{name}

Requires:	%{name}%{?_isa}		== %{version}-%{release}

%description devel
This package contains libraries and header files for
developing applications that use %{name}.


%package doc
Summary:	Reference manual for json-c

BuildArch:	noarch

BuildRequires:	doxygen
BuildRequires:	hardlink

%description doc
This package contains the reference manual for json-c.


%prep
%autosetup -n %{origname}-%{origname}-%{version}-%{reldate}

for doc in ChangeLog; do
	%{_bindir}/iconv -f iso-8859-1 -t utf8 ${doc} > ${doc}.new
	/bin/touch -r ${doc} ${doc}.new
	%{__mv} -f ${doc}.new ${doc}
done

%{__sed} -i 's|-Werror ||g' Makefile.am.inc

# For the compatibility package
%{__sed} -i 's|json-c.pc|json-c12.pc|g' Makefile.am
%{__sed} -i 's|libjson-c|libjson-c12|g' Makefile.am
%{__sed} -i 's|libjson_c|libjson_c12|g' Makefile.am
%{__sed} -i 's|/json-c|/json-c12|g' Makefile.am
%{__sed} -i 's|libjson-c|libjson-c12|g' tests/Makefile.am

%{__sed} -i 's|json-c.pc|json-c12.pc|g' configure.ac
%{__sed} -i 's|json-c-uninstalled.pc|json-c12-uninstalled.pc|g' configure.ac
%{__sed} -i 's|AM_PROG_LIBTOOL|LT_INIT|g' configure.ac

%{__sed} -i 's|ljson-c|ljson-c12|g' json-c.pc.in
%{__sed} -i 's|ljson-c|ljson-c12|g' json-c-uninstalled.pc.in
%{__mv} json-c.pc.in json-c12.pc.in
%{__mv} json-c-uninstalled.pc.in json-c12-uninstalled.pc.in
%{__mv} json-c.vcproj json-c12.vcproj

%{_bindir}/autoupdate -v
%{_bindir}/autoreconf -fiv


%build
%configure			\
	--disable-rpath		\
	--disable-silent-rules	\
	--disable-static	\
	--enable-shared		\
	--enable-rdrand
%make_build

%{_bindir}/doxygen Doxyfile


%install
%make_install
%{_bindir}/find %{buildroot} -name '*.la' -delete -print

%{__mkdir} -p %{buildroot}/%{_pkgdocdir}
%{__cp} -pr doc/html ChangeLog README README.* %{buildroot}/%{_pkgdocdir}
%{_sbindir}/hardlink -cv %{buildroot}/%{_pkgdocdir}


%check
%make_build check


%pretrans devel -p <lua>
path = "%{_includedir}/%{origname}"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc %dir %{_pkgdocdir}
%license AUTHORS
%license COPYING
%{_libdir}/lib%{name}.so.*


%files devel
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/ChangeLog
%doc %{_pkgdocdir}/README*
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%files doc
%if 0%{?fedora} || 0%{?rhel} >= 7
%license %{_datadir}/licenses/%{name}*
%endif # 0%%{?fedora} || 0%%{?rhel} >= 7
%doc %{_pkgdocdir}


%changelog
* Mon May 8 2017 Jeffrey Lau <jeffrey.lau@ribose.com> - 0.12.1-1
- Initial compat-package for EPEL >= 6, based on json-c from recent Fedora

* Thu Apr 27 2017 Björn Esser <besser82@fedoraproject.org> - 0.12.1-1
- Update to new upstream release
- Introduces SONAME bump, that should have been in 0.12 already
- Unify %%doc
- General spec-file cleanup

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Christopher Meng <rpm@cicku.me> - 0.12-4
- SONAME bump postponed.

* Mon Jul 28 2014 Christopher Meng <rpm@cicku.me> - 0.12-3
- SONAME bump, see bug 1123785

* Fri Jul 25 2014 Christopher Meng <rpm@cicku.me> - 0.12-2
- NVR bump

* Thu Jul 24 2014 Christopher Meng <rpm@cicku.me> - 0.12-1
- Update to 0.12

* Sat Jul 12 2014 Tom Callaway <spot@fedoraproject.org> - 0.11-8
- fix license handling

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 09 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.11-7
- Address CVE-2013-6371 and CVE-2013-6370 (BZ #1085676 and #1085677).
- Enabled rdrand support.

* Mon Feb 10 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.11-6
- Bump spec.

* Sat Dec 21 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.11-5
- Run test suite during build.
- Drop empty NEWS from docs.

* Tue Sep 10 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.11-4
- Remove default warning flags so that package builds on EPEL as well.

* Sat Aug 24 2013 Remi Collet <remi@fedoraproject.org> - 0.11-3
- increase parser strictness for php

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Remi Collet <remi@fedoraproject.org> - 0.11-1
- update to 0.11
- fix source0
- enable both json and json-c libraries

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 24 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.10-2
- Compile and install json_object_iterator using Remi Collet's fix (BZ #879771).

* Sat Nov 24 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.10-1
- Update to 0.10 (BZ #879771).

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 23 2012 Jiri Pirko <jpirko@redhat.com> - 0.9-4
- add json_tokener_parse_verbose, and return NULL on parser errors

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Apr 06 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.9-1
- First release.
