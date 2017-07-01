%global reldate 20170509
%global script_name checkpatch.pl

Name:		checkpatch
Version:	%{reldate}
Release:	1%{?dist}
Summary:	%{script_name} is a coding style checker from the Linux kernel.

License:	GPLv2
URL:	   	https://github.com/torvalds/linux
Source0:	%{url}/raw/master/scripts/checkpatch.pl
Source1:	%{url}/raw/master/scripts/spelling.txt
Source2:	%{url}/raw/master/COPYING
Source3:	https://github.com/riboseinc/retrace/raw/master/ci/checkpatch.pl.patch

BuildArch:	noarch
Requires: perl

%description
%{script_name} is a script in the Linux kernel tree that facilitates better
kernel code, and can be used to check many coding style rules.

%prep
%setup -T -c -n %{name}
%{__cp} -a %{SOURCE0} .
%{__cp} -a %{SOURCE1} .
%{__cp} -a %{SOURCE2} .
patch -p0 < %{SOURCE3}
echo "invalid.struct.name" > const_structs.checkpatch

%build

%install

chmod a+x %{script_name}
%{__mkdir} -p %{buildroot}/%{_datadir}/%{name}
%{__mkdir} -p %{buildroot}/%{_bindir}

%{__cp} -a %{script_name} %{buildroot}/%{_datadir}/%{name}
%{__cp} -a COPYING %{buildroot}/%{_datadir}/%{name}
%{__cp} -a spelling.txt %{buildroot}/%{_datadir}/%{name}
%{__cp} -a const_structs.checkpatch %{buildroot}/%{_datadir}/%{name}

pushd %{buildroot}/%{_bindir}
%{__ln_s} -s ../..%{_datadir}/%{name}/%{script_name} .
popd


%files
%license COPYING
%{_bindir}/*
%{_datadir}/*

%changelog
* Sat Jul 1 2017 Ronald Tse <ronald.tse@ribose.com> - 20170509-1
- Initial spec.

