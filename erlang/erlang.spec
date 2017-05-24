# spec file for package erlang
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%global debug_package %{nil}


Name:           erlang
Epoch:          2
Version:        R15B01
Release:        1%{?dist}
License:        Erlang Public License
Summary:        General-purpose programming language and runtime environment
Url:            http://www.erlang.org
Group:          Development/Languages/Other
Source:         http://pkgs.fedoraproject.org/repo/pkgs/erlang/otp_src_R15B01.tar.gz/f12d00f6e62b36ad027d6c0c08905fad/otp_src_R15B01.tar.gz
#Source:        http://www.erlang.org/download/otp_src_%{version}.tar.gz
Source1:        http://pkgs.fedoraproject.org/repo/pkgs/erlang/otp_doc_html_R15B01.tar.gz/7569cae680eecd64e7e5d952be788ee5/otp_doc_html_R15B01.tar.gz
#Source1:       http://www.erlang.org/download/otp_doc_html_%{version}.tar.gz
Source2:        http://pkgs.fedoraproject.org/repo/pkgs/erlang/otp_doc_man_R15B01.tar.gz/d87412c2a1e6005bbe29dfe642a9ca20/otp_doc_man_R15B01.tar.gz
#Source2:       http://www.erlang.org/download/otp_doc_man_%{version}.tar.gz
Source3:        %{name}-rpmlintrc
# PATCH-MISSING-TAG -- See http://en.opensuse.org/openSUSE:Packaging_Patches_guidelines
#Patch0:         otp-R15B01-rpath.patch
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  openssh
BuildRequires:  openssl-devel
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  unixODBC-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} >= 1140
BuildRequires:  java-1_7_0-openjdk-devel
%else
BuildRequires:  java-devel >= 1.5.0
%endif
#BuildRequires:  Mesa-devel
BuildRequires:  krb5-devel
%if 0%{?sles_version} >= 10
BuildRequires:  update-alternatives
%endif
%if 0%{?suse_version} > 1020
BuildRequires:  fdupes
%endif

%if 0%{?suse_version} >= 1140
BuildRequires:  wxWidgets
BuildRequires:  wxWidgets-wxcontainer-devel
%define _use_internal_dependency_generator 0
%define __find_requires %wx_requires
%else
BuildRequires:  wxGTK-devel >= 2.8
%endif

%description
Erlang is a general-purpose programming language and runtime
environment. Erlang has built-in support for concurrency, distribution
and fault tolerance. Erlang is used in several large telecommunication
systems from Ericsson.

%package debugger
Summary:        A debugger for debugging and testing of Erlang programs
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-gs = %{version}
Requires:       %{name}-wx = %{version}

%description debugger
A debugger for debugging and testing of Erlang programs.

%package dialyzer
Summary:        A DIscrepany AnaLYZer for ERlang programs
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-gs = %{version}
Requires:       %{name}-wx = %{version}

%description dialyzer
A DIscrepany AnaLYZer for ERlang programs.

%package doc
Summary:        Erlang documentation
Group:          Development/Languages/Other
#Recommends:     %{name} = %{version}

%description doc
Documentation for Erlang.

%package et
Summary:        An event tracer for Erlang programs
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-gs = %{version}
Requires:       %{name}-wx = %{version}

%description et
An event tracer for Erlang programs.

%package jinterface
Summary:        Erlang Java Interface
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}
Requires:       java >= 1.5.0

%description jinterface
JInterface module for accessing erlang from Java

%package gs
Summary:        A library for Tcl/Tk support in Erlang
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       tk

%description gs
A Graphics System used to write platform independent user interfaces.

%package reltool
Summary:        A release management tool
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-gs = %{version}
Requires:       %{name}-wx = %{version}

%description reltool
Reltool is a release management tool. It analyses a given
Erlang/OTP installation and determines various dependencies
between applications. The graphical frontend depicts the
dependencies and enables interactive customization of a
target system. The backend provides a batch interface
for generation of customized target systems.

%package src
Summary:        Erlang/OTP applications sources
Group:          Development/Languages/Other
Requires:       %{name} = %{version}

%description src
Erlang sources for all the applications in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package toolbar
Summary:        A tool bar simplifying access to the Erlang tools
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-gs = %{version}

%description toolbar
A tool bar simplifying access to the Erlang tools.

%package tv
Summary:        An ETS and MNESIA graphical table visualizer
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-gs = %{version}

%description tv
An ETS and MNESIA graphical table visualizer.

%package wx
Summary:        A library for wxWidgets support in Erlang
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
%if 0%{?suse_version} >= 1140
Requires:       wxWidgets >= 2.8
%else
Requires:       wxGTK >= 2.8
%endif

%description wx
A Graphics System used to write platform independent user interfaces.

%prep
%setup -q -n otp_src_%{version}
#%patch0 -p1 -b .rpath

chmod -R u+w .
# enable dynamic linking for ssl
sed -i 's|SSL_DYNAMIC_ONLY=no|SSL_DYNAMIC_ONLY=yes|' erts/configure
# Remove shipped zlib sources
#rm -f erts/emulator/zlib/*.[ch]

# fix for arch linux bug #17001 (wx not working)
sed -i 's|WX_LIBS=`$WX_CONFIG_WITH_ARGS --libs`|WX_LIBS="`$WX_CONFIG_WITH_ARGS --libs` -lGLU"|' lib/wx/configure || return 1

%build
# we need build only 1.5 target for java
# for SLE only
%if 0%{?sles_version} >= 10 || 0%{?suse_version} >= 1110
    export JAVAC="javac -target 1.5"
%endif
%if 0%{?suse_version} == 1100 || 0%{?fedora_version} == 9
export CFLAGS="-fno-strict-aliasing"
%else
export CFLAGS="%{optflags} -fno-strict-aliasing"
%endif
export CXXFLAGS=$CFLAGS

%configure \
    --disable-rpath \
    --with-ssl=%{_prefix} \
    --enable-threads \
    --enable-smp-support \
    --enable-kernel-poll \
    --enable-hipe \
    --enable-shared-zlib
make
# parallel builds do not work (yet) - last tested with R14B04
# make %{?_smp_mflags}

%install
#%if 0%{?sles_version} >= 10
    #make DESTDIR=%{buildroot} install
#%else
    %make_install
#%endif

export TOOLS_VERSION=`ls %{buildroot}%{_libdir}/erlang/lib/ |grep ^tools- | sed "s|tools-||"`

# clean up
find %{buildroot}%{_libdir}/erlang -perm 0775 | xargs chmod -v 0755
find %{buildroot}%{_libdir}/erlang -name Makefile | xargs chmod -v 0644
find %{buildroot}%{_libdir}/erlang -name \*.bat | xargs rm -fv
find %{buildroot}%{_libdir}/erlang -name index.txt.old | xargs rm -fv
rm %{buildroot}%{_libdir}/erlang/lib/tools-$TOOLS_VERSION/emacs/test.erl.orig
mv %{buildroot}%{_libdir}/erlang/lib/tools-$TOOLS_VERSION/emacs/test.erl.indented %{buildroot}%{_libdir}/erlang/lib/tools-$TOOLS_VERSION/emacs/test.erl

# doc
mv README.md README
mkdir -p erlang_doc
tar -C erlang_doc -xzf %{SOURCE1}
tar -C %{buildroot}/%{_libdir}/erlang -xzf %{SOURCE2}
# compress man pages ...
find %{buildroot}%{_libdir}/erlang/man -type f -exec gzip {} +

#make link to OtpErlang-*.jar in %%{_javadir}
mkdir -p %{buildroot}%{_javadir}
cd %{buildroot}%{_javadir}
export JINTERFACE_VERSION=`ls %{buildroot}%{_libdir}/erlang/lib/ |grep ^jinterface- | sed "s|jinterface-||"`
ln -sf ../../%{_lib}/erlang/lib/jinterface-$JINTERFACE_VERSION/priv/OtpErlang.jar OtpErlang-$JINTERFACE_VERSION.jar
cd -

# emacs: automatically load support for erlang
# http://lists.mandriva.com//bugs/2007-08/msg00930.php
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp
cat > %{buildroot}%{_datadir}/emacs/site-lisp/erlang.el << EOF
(setq load-path (cons "%{_libdir}/erlang/lib/tools-$TOOLS_VERSION/emacs" load-path))
(add-to-list 'load-path "%{_datadir}/emacs/site-lisp/ess")
(load-library "erlang-start")
EOF

%if 0%{?suse_version} > 1020
# hardlink duplicates:
%fdupes %{buildroot}/%{_libdir}/erlang
# %%doc macro copies the files to the package doc dir, hardlinks thus don't work
%fdupes -s erlang_doc
%endif

%post
%{_libdir}/erlang/Install -minimal %{_libdir}/erlang >/dev/null 2>/dev/null

%files
%defattr(-,root,root)
%doc AUTHORS EPLICENCE README
%doc %{_libdir}/erlang/PR.template
%doc %{_libdir}/erlang/README
%doc %{_libdir}/erlang/COPYRIGHT
%{_bindir}/*
%dir %{_libdir}/erlang
%dir %{_libdir}/erlang/lib/
%exclude %{_libdir}/erlang/lib/*/src
%exclude %{_libdir}/erlang/lib/*/c_src
%exclude %{_libdir}/erlang/lib/*/java_src
%{_libdir}/erlang/bin/
%{_libdir}/erlang/erts-*/
%{_libdir}/erlang/lib/appmon-*/
%{_libdir}/erlang/lib/asn1-*/
%{_libdir}/erlang/lib/common_test-*/
%{_libdir}/erlang/lib/compiler-*/
%{_libdir}/erlang/lib/cosEvent-*/
%{_libdir}/erlang/lib/cosEventDomain-*/
%{_libdir}/erlang/lib/cosFileTransfer-*/
%{_libdir}/erlang/lib/cosNotification-*/
%{_libdir}/erlang/lib/cosProperty-*/
%{_libdir}/erlang/lib/cosTime-*/
%{_libdir}/erlang/lib/cosTransactions-*/
%{_libdir}/erlang/lib/crypto-*/
%{_libdir}/erlang/lib/diameter-*/
%{_libdir}/erlang/lib/edoc-*/
%{_libdir}/erlang/lib/eldap-*/
%{_libdir}/erlang/lib/erl_docgen-*/
%{_libdir}/erlang/lib/erl_interface-*/
%{_libdir}/erlang/lib/erts-*/
%{_libdir}/erlang/lib/eunit-*/
%{_libdir}/erlang/lib/hipe-*/
%{_libdir}/erlang/lib/ic-*/
%{_libdir}/erlang/lib/inets-*/
%{_libdir}/erlang/lib/inviso-*/
%{_libdir}/erlang/lib/kernel-*/
%{_libdir}/erlang/lib/megaco-*/
%{_libdir}/erlang/lib/mnesia-*/
%{_libdir}/erlang/lib/observer-*/
%{_libdir}/erlang/lib/odbc-*/
%{_libdir}/erlang/lib/orber-*/
%{_libdir}/erlang/lib/os_mon-*/
%{_libdir}/erlang/lib/otp_mibs-*/
%{_libdir}/erlang/lib/parsetools-*/
%{_libdir}/erlang/lib/percept-*/
%{_libdir}/erlang/lib/pman-*/
%{_libdir}/erlang/lib/public_key-*/
%{_libdir}/erlang/lib/runtime_tools-*/
%{_libdir}/erlang/lib/sasl-*/
%{_libdir}/erlang/lib/snmp-*/
%{_libdir}/erlang/lib/ssh-*/
%{_libdir}/erlang/lib/ssl-*/
%{_libdir}/erlang/lib/stdlib-*/
%{_libdir}/erlang/lib/syntax_tools-*/
%{_libdir}/erlang/lib/test_server-*/
%{_libdir}/erlang/lib/tools-*/
%{_libdir}/erlang/lib/typer-*/
%{_libdir}/erlang/lib/webtool-*/
%{_libdir}/erlang/lib/xmerl-*/
%{_libdir}/erlang/man/
%{_libdir}/erlang/misc/
%{_libdir}/erlang/releases/
%{_libdir}/erlang/usr/
%{_libdir}/erlang/Install
%{_datadir}/emacs/site-lisp/erlang.el

%files debugger
%defattr(-,root,root)
%{_libdir}/erlang/lib/debugger-*/
%exclude %{_libdir}/erlang/lib/debugger-*/src

%files dialyzer
%defattr(-,root,root)
%{_libdir}/erlang/lib/dialyzer-*/
%exclude %{_libdir}/erlang/lib/dialyzer-*/src

%files doc
%defattr(-,root,root)
%doc erlang_doc/*

%files et
%defattr(-,root,root)
%{_libdir}/erlang/lib/et-*/
%exclude %{_libdir}/erlang/lib/et-*/src

%files gs
%defattr(-,root,root)
%{_libdir}/erlang/lib/gs-*/
%exclude %{_libdir}/erlang/lib/gs-*/src

%files jinterface
%defattr(-,root,root,-)
%{_libdir}/erlang/lib/jinterface-*/
%exclude %{_libdir}/erlang/lib/jinterface-*/java_src
%{_javadir}/*

%files reltool
%defattr(-,root,root)
%{_libdir}/erlang/lib/reltool-*/
%exclude %{_libdir}/erlang/lib/reltool-*/src

%files src
%defattr(-,root,root)
%exclude %{_libdir}/erlang/lib/erl_interface-*/src/INSTALL
%{_libdir}/erlang/lib/*/src
%{_libdir}/erlang/lib/*/c_src
%{_libdir}/erlang/lib/*/java_src

%files toolbar
%defattr(-,root,root)
%{_libdir}/erlang/lib/toolbar-*/
%exclude %{_libdir}/erlang/lib/toolbar-*/src

%files tv
%defattr(-,root,root)
%{_libdir}/erlang/lib/tv-*/
%exclude %{_libdir}/erlang/lib/tv-*/src

%files wx
%defattr(-,root,root)
%{_libdir}/erlang/lib/wx-*/
%exclude %{_libdir}/erlang/lib/wx-*/src

%changelog

* Fri May 19 2017 Ronald Tse <ronald.tse@ribose.com> - R15B01-1
- Build package R15B01

