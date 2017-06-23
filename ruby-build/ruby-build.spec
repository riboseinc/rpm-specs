Name:          ruby-build
Version:       20170523
Release:       1%{?dist}
Group:         Applications/System
Summary:       The ruby-build program for building Ruby instances.
BuildArch:     noarch
License:       MIT
URL:           https://github.com/rbenv/ruby-build
Source0:       %{url}/archive/v%{version}.tar.gz

BuildRequires: redhat-rpm-config

# For compiling rubies
Requires: openssl-devel readline-devel zlib-devel readline libyaml libyaml-devel readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make libffi-devel

# For running rubies
Requires: openssl libyaml

%description
Installs %{name}.

%prep
%setup

%build

%install
PREFIX=%{buildroot}/%{_prefix} \
  ./install.sh
%{__mkdir} -p %{buildroot}/%{_pkgdocdir}
%{__mv} README.md LICENSE %{buildroot}/%{_pkgdocdir}

%files
%doc %{_pkgdocdir}
%{_bindir}/*
%{_datarootdir}/%{name}
%license %{_pkgdocdir}/LICENSE

%changelog
* Fri Jun 23 2017 Ronald Tse <ronald.tse@ribose.com> - 20170523
- Initial commit

