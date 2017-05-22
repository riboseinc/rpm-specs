%global realname exmpp
%global reldate 20160607
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		erlang-exmpp
Version:	0.9.9
Release:	1%{?dist}
Summary:	An Erlang XMPP library
Group:		Development/Languages
License:	ERPL
URL:		https://github.com/processone/%{realname}
Source0:	%{url}/archive/v%{version}.tar.gz

BuildRequires:	autoconf automake libtool
BuildRequires:	erlang >= R15B01
BuildRequires:	expat-devel
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	git
Provides:	%{realname} = %{version}-%{release}


%description
Erlang XMPP library (exmpp) is a fast and scalable library for the eXtensible
Messaging and Presence Protocol.


%prep
#Requires:	%{name}%{?_isa}		== %{version}-%{release}
%autosetup -n %{realname}-%{version}
#%{__sed} -i 's|-Werror ||g' Makefile.am.inc
%{_bindir}/autoreconf -fiv

%build
#%configure
%configure --prefix=%{_libdir}/erlang/lib
%make_build

%install
%make_install
%{_bindir}/find %{buildroot} -name '*.la' -delete -print

%{__mkdir} -p %{buildroot}/%{_pkgdocdir}
%{_sbindir}/hardlink -cvf %{buildroot}/%{_pkgdocdir}


%files
%doc %dir %{_pkgdocdir}
%doc %{_libdir}/erlang/lib/%{realname}-%{version}/doc/html/*

%dir %{_libdir}/erlang/lib/%{realname}-%{version}
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/ebin
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/include
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/include/internal
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/priv
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/priv/lib
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/exmpp.app
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/exmpp.appup
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/exmpp*.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/include/*.hrl
%{_libdir}/erlang/lib/%{realname}-%{version}/include/internal/*.hrl
%{_libdir}/erlang/lib/%{realname}-%{version}/priv/lib/*.so


%changelog
* Mon May 22 2017 Ronald Tse <ronald.tse@ribose.com> - 0.12.1-2
- Update package to work with 0.12.1 properly

* Mon May 8 2017 Jeffrey Lau <jeffrey.lau@ribose.com> - 0.12.1-1
- Change package name to json-c12 to prevent breaking compatability with 0.11.x

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
