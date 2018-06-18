Summary:  	Shell tool for executing jobs in parallel
Name: 	  	parallel
Version:   	20180522
Release:   	1
License:   	GPL
Group: 	  	Productivity/File utilities
URL: 		    https://ftp.gnu.org/gnu/parallel
Source0:  	%{url}/%{name}-%{version}.tar.bz2
BuildArch:	noarch
#BuildArchitectures: noarch
BuildRequires: bzip2 make perl
Requires: perl

%description
GNU Parallel is a shell tool for executing jobs in parallel using one
or more computers. A job can be a single command or a small script
that has to be run for each of the lines in the input. The typical
input is a list of files, a list of hosts, a list of users, a list of
URLs, or a list of tables. A job can also be a command that reads from
a pipe. GNU Parallel can then split the input and pipe it into
commands in parallel.

If you use xargs and tee today you will find GNU Parallel very easy to
use as GNU Parallel is written to have the same options as xargs. If
you write loops in shell, you will find GNU Parallel may be able to
replace most of the loops and make them run faster by running several
jobs in parallel.

GNU Parallel makes sure output from the commands is the same output as
you would get had you run the commands sequentially. This makes it
possible to use output from GNU Parallel as input for other programs.

For each line of input GNU Parallel will execute command with the line
as arguments. If no command is given, the line of input is
executed. Several lines will be run in parallel. GNU Parallel can
often be used as a substitute for xargs or cat | bash.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
%{__mv} %{buildroot}/%{_docdir}/%{name} %{buildroot}/%{_pkgdocdir}

%files
%doc README NEWS
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man7/*

%changelog
* Sun Jun 18 2018 Ronald Tse <ronald.tse@ribose.com> - 20180522-1.0
- Upgrade to 20180522

* Thu Jun 29 2017 Ronald Tse <ronald.tse@ribose.com> - 20170622-1.0
- Upgrade to 20170622
- Cleanup spec

* Thu Apr 24 2014 Ivan Polonevich <joni @ wargaming dot net> - 20140422-2.1
- Rebuild for WG

* Thu Apr 24 2014 Ivan Polonevich <joni @ wargaming dot net> - 20140422-2.1
- Rebuild for WG

* Sat Jan 22 2011 Ole Tange
- Upgrade to 20110122

* Wed Dec 22 2010 Ole Tange
- Upgrade to 20101222

* Wed Sep 22 2010 Ole Tange
- Upgrade to 20100922

* Mon Sep 06 2010 Ole Tange
- Upgrade to current git-version of source. Tested on build.opensuse.org

* Fri Aug 27 2010 Ole Tange
- Untested upgrade to current git-version of source.

* Sun Aug 08 2010 Markus Ammer
- Initial package setup.

