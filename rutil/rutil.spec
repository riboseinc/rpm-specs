%global gopath /usr/share/gocode

# [GitHub]
%global commit0 e149910e5dd6fb32b5dd479d6090f9748a82d67a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gorepo github.com/pampa/%{name}

# To resolve: "ERROR: No build ID note found"
# We don't build a debuginfo package
%undefine _missing_build_ids_terminate_build

Summary:  	rutil in Go
Name: 	  	rutil
Version:   	0.1.2
Release:   	1
License:   	UNLICENSE
Group: 	  	Productivity/File utilities
URL: 		    https://%{gorepo}
Source0:    %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
#BuildArchitectures: noarch
BuildRequires: go make git
Requires: go

%description

%prep
# GitHub archive format
%autosetup -n %{name}-%{commit0}

%build
export GOPATH=%{gopath}
export GOBIN=${GOPATH}/bin
go get ./...

%install
%{__mkdir} -p %{buildroot}/%{_bindir}
%{__mv} -f %{gopath}/bin/%{name}-%{commit0} %{buildroot}/%{_bindir}/%{name}

%files
%doc README.md
%license UNLICENSE
%{_bindir}/*

%changelog
* Thu Jun 29 2017 Ronald Tse <ronald.tse@ribose.com> - 0.1.2-1
- Initial spec
