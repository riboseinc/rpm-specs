%global realname xmlrpc
%global reldate 20160607
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		erlang-xmlrpc
Epoch:    1
Version:	1.13
Release:	1
Summary:	An Erlang XML-RPC library
Group:		Development/Languages
License:	ERPL
URL:		http://www.ejabberd.im
Source0:	%{url}/files/contributions/%{realname}-%{version}-ipr2.tgz

BuildRequires:	autoconf automake libtool
BuildRequires:	erlang >= R15B01
Provides:	%{realname} = %{version}-%{release}


%description
An HTTP 1.1 compliant XML-RPC library for Erlang. It is designed to make it
easy to write XML-RPC Erlang clients and/or servers. The library is compliant
with the XML-RPC specification published by http://www.xmlrpc.org/.

%prep
%autosetup -n %{realname}-%{version}

%build
pushd src
make
%{__mkdir} ../include
%{__mv} *.hrl ../include
popd
%{__rm} -rf src/ examples/ *.diff CHANGES TODO

%install
%{__mkdir} -p %{buildroot}/%{_libdir}/erlang/lib
%{__cp} -ra %{_builddir}/%{realname}-%{version} %{buildroot}/%{_libdir}/erlang/lib/
%{__mkdir} -p %{buildroot}/%{_pkgdocdir}

%files
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/ebin
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/include
%{_libdir}/erlang/lib/%{realname}-%{version}/xmlrpc.pub
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/*.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/include/*.hrl

%doc %dir %{_pkgdocdir}
%doc %{_libdir}/erlang/lib/%{realname}-%{version}/README
%doc %{_libdir}/erlang/lib/%{realname}-%{version}/doc/
%license %{_libdir}/erlang/lib/%{realname}-%{version}/LICENSE

%changelog
* Wed May 24 2017 Ronald Tse <ronald.tse@ribose.com> - 1.13-1
- Initial spec
