%global major_version 2
%global minor_version 3
%global teeny_version 4
%global major_minor_version %{major_version}.%{minor_version}

%global ruby_version %{major_minor_version}.%{teeny_version}
%global ruby_release %{ruby_version}
%global ruby_archive %{name}-%{ruby_version}
#%global revision 58214

# If revision and milestone are removed/commented out, the official release
# build is expected.
%if 0%{?milestone:1}%{?revision:1} != 0
%global development_release %{?milestone}%{?!milestone:%{?revision:r%{revision}}}
%global ruby_archive %{ruby_archive}-%{?milestone}%{?!milestone:%{?revision:r%{revision}}}
%endif

%global release 62
%{!?release_string:%global release_string %{?development_release:0.}%{release}%{?development_release:.%{development_release}}%{?dist}}

### DIRS

# TODO: define prefxi
%global _prefix /usr/local/%{name}

%global ruby_libdir %{_datadir}/%{name}
%global ruby_libarchdir %{_libdir}/%{name}

# This is the local lib/arch and should not be used for packaging.
%global ruby_sitedir site_ruby
%global ruby_sitelibdir %{_prefix}/local/share/%{name}/%{ruby_sitedir}
%global ruby_sitearchdir %{_prefix}/local/%{_lib}/%{name}/%{ruby_sitedir}

# This is the general location for libs/archs compatible with all
# or most of the Ruby versions available in the Fedora repositories.
%global ruby_vendordir vendor_ruby
%global ruby_vendorlibdir %{ruby_libdir}/%{ruby_vendordir}
%global ruby_vendorarchdir %{ruby_libarchdir}/%{ruby_vendordir}

%global rbenv_path ~/.rbenv

# The RubyGems root folder.
%global gem_dir %{_datadir}/gems
%endif

Name:		rbenv-ruby-%{ruby_version}
Version:	%{ruby_version}
Release:  %{release_string}
#Release:	1%{?dist}
Group: 		Development/Languages
Summary: 	A ruby instance that can co-exist with other instances in the rbenv (RPM) ecosystem.
License: 	MIT
URL: http://ruby-lang.org/
Source0: ftp://ftp.ruby-lang.org/pub/%{name}/%{major_minor_version}/%{ruby_archive}.tar.xz
Source1: operating_system.rb
# This wrapper fixes https://bugzilla.redhat.com/show_bug.cgi?id=977941
# Hopefully, it will get removed soon:
# https://fedorahosted.org/fpc/ticket/312
# https://bugzilla.redhat.com/show_bug.cgi?id=977941
Source2: config.h

# Fix ruby_version abuse.
# https://bugs.ruby-lang.org/issues/11002
Patch0: ruby-2.3.0-ruby_version.patch
# http://bugs.ruby-lang.org/issues/7807
Patch1: ruby-2.1.0-Prevent-duplicated-paths-when-empty-version-string-i.patch
# Allows to override libruby.so placement. Hopefully we will be able to return
# to plain --with-rubyarchprefix.
# http://bugs.ruby-lang.org/issues/8973
Patch2: ruby-2.1.0-Enable-configuration-of-archlibdir.patch
# Force multiarch directories for i.86 to be always named i386. This solves
# some differencies in build between Fedora and RHEL.
Patch3: ruby-2.1.0-always-use-i386.patch
# Allows to install RubyGems into custom directory, outside of Ruby's tree.
# http://bugs.ruby-lang.org/issues/5617
Patch4: ruby-2.1.0-custom-rubygems-location.patch
# Make mkmf verbose by default
Patch5: ruby-1.9.3-mkmf-verbose.patch
# Adds support for '--with-prelude' configuration option. This allows to built
# in support for ABRT.
# http://bugs.ruby-lang.org/issues/8566
Patch6: ruby-2.1.0-Allow-to-specify-additional-preludes-by-configuratio.patch
# Use miniruby to regenerate prelude.c.
# https://bugs.ruby-lang.org/issues/10554
Patch7: ruby-2.2.3-Generate-preludes-using-miniruby.patch
# Workaround "an invalid stdio handle" error on PPC, due to recently introduced
# hardening features of glibc (rhbz#1361037).
# https://bugs.ruby-lang.org/issues/12666
Patch9: ruby-2.3.1-Rely-on-ldd-to-detect-glibc.patch


BuildRequires: 	redhat-rpm-config readline libyaml libyaml-devel readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make libffi-devel openssl-devel
Requires: 	libyaml openssl rbenv

BuildRequires: autoconf
BuildRequires: gdbm-devel
BuildRequires: libffi-devel
#BuildRequires: compat-openssl10-devel
BuildRequires: openssl-devel
BuildRequires: libyaml-devel
BuildRequires: readline-devel
BuildRequires: tk-devel
# Needed to pass test_set_program_name(TestRubyOptions)
BuildRequires: procps
BuildRequires: %{_bindir}/dtrace
# RubyGems test suite optional dependencies.
BuildRequires: git
BuildRequires: %{_bindir}/cmake

## TODO: add Provides and Obsoletes

# This package provides %%{_bindir}/ruby-mri therefore it is marked by this
# virtual provide. It can be installed as dependency of rubypick.
Provides: ruby(runtime_executable) = %{ruby_release}

%description
Installs Ruby in a location that rbenv (from RPM) can manage, thereby allowing
several versions to co-exist.

%prep
%setup -q -n %{ruby_archive}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch9 -p1

%build
autoconf

# Ruby does not respec LDFLAGS :(
# https://bugs.ruby-lang.org/issues/11863
export EXTLDFLAGS="%{__global_ldflags}"

#export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

%configure \
        --with-rubylibprefix='%{ruby_libdir}' \
        --with-archlibdir='%{_libdir}' \
        --with-rubyarchprefix='%{ruby_libarchdir}' \
        --with-sitedir='%{ruby_sitelibdir}' \
        --with-sitearchdir='%{ruby_sitearchdir}' \
        --with-vendordir='%{ruby_vendorlibdir}' \
        --with-vendorarchdir='%{ruby_vendorarchdir}' \
        --with-rubyhdrdir='%{_includedir}' \
        --with-rubyarchhdrdir='%{_includedir}' \
        --with-sitearchhdrdir='$(sitehdrdir)/$(arch)' \
        --with-vendorarchhdrdir='$(vendorhdrdir)/$(arch)' \
        --with-rubygemsdir='%{rubygems_dir}' \
        --with-ruby-pc='%{name}.pc' \
        --disable-rpath \
        --enable-shared \
        --with-ruby-version='' \
        --enable-multiarch
#\
#--with-prelude=./abrt_prelude.rb \

#__OLD__

# Q= makes the build output more verbose and allows to check Fedora
# compiler options.
%make_build COPY="cp -p" Q=

%install
%make_install
# delete source, doc and debug (all in usr dir which we don't want to install)
%{__rm} -rf %{buildroot}/usr

# Rename ruby/config.h to ruby/config-<arch>.h to avoid file conflicts on
# multilib systems and install config.h wrapper
mv %{buildroot}%{_includedir}/%{name}/config.h %{buildroot}%{_includedir}/%{name}/config-%{_arch}.h
install -m644 %{SOURCE7} %{buildroot}%{_includedir}/%{name}/config.h

# Version is empty if --with-ruby-version is specified.
# http://bugs.ruby-lang.org/issues/7807
sed -i 's/Version: \${ruby_version}/Version: %{ruby_version}/' %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

# Kill bundled certificates, as they should be part of ca-certificates.
for cert in \
  Class3PublicPrimaryCertificationAuthority.pem \
  DigiCertHighAssuranceEVRootCA.pem \
  EntrustnetSecureServerCertificationAuthority.pem \
  GeoTrustGlobalCA.pem \
  AddTrustExternalCARoot.pem \
  AddTrustExternalCARoot-2048.pem \
  GlobalSignRootCA.pem
do
  rm %{buildroot}%{rubygems_dir}/rubygems/ssl_certs/$cert
done
# Ensure there is not forgotten any certificate.
test ! "$(ls -A  %{buildroot}%{rubygems_dir}/rubygems/ssl_certs/ 2>/dev/null)"

# Install dependency generators.
mkdir -p %{buildroot}%{_rpmconfigdir}/fileattrs
install -m 644 %{SOURCE8} %{buildroot}%{_rpmconfigdir}/fileattrs
install -m 755 %{SOURCE9} %{buildroot}%{_rpmconfigdir}
install -m 755 %{SOURCE10} %{buildroot}%{_rpmconfigdir}

# Install custom operating_system.rb.
mkdir -p %{buildroot}%{rubygems_dir}/rubygems/defaults
cp %{SOURCE1} %{buildroot}%{rubygems_dir}/rubygems/defaults

## RBENV-SPECIFIC
# setup symbolic link and global version for users
%define system_profile_directory %{buildroot}/%{_sysconfdir}/profile.d
install -m 0755 -d %{system_profile_directory}
%define profile_rbenv_ruby_script_filename %{system_profile_directory}/%{name}.sh
cat > %{profile_rbenv_ruby_script_filename} <<END_OF_RBENV_RUBY_PROFILE
# add rbenv ruby path symlink
if [ ! -h %{rbenv_path}/versions/%{ruby_version} ]
  then
    ln -s %{_prefix} %{rbenv_path}/versions/%{ruby_version}
    eval "$(rbenv rehash)"
fi
# add global ruby version if needed.
if [ ! -e %{rbenv_path}/version ]
  then
    echo "%{ruby_version}" > %{rbenv_path}/version
fi
END_OF_RBENV_RUBY_PROFILE
chmod a+x %{profile_rbenv_ruby_script_filename}

%post
echo " "
echo "rbenv enabled Ruby has been installed in %{_prefix}. Log in again to activate."

%files
%dir %{_prefix}
%{_prefix}/*
%{_sysconfdir}/profile.d
%{_sysconfdir}/profile.d/rbenv-ruby_%{ruby_version}.sh

%changelog
* Sun May 07 2017 Aaron Smith <ajsmith10381@gmail.com> - 2.3.4
- Updating to use 2.3.4

* Mon Mar 31 2014 Guy Gershoni <guy@conchus.com> - p76-2
Making /etc/profile.d/rbenv-ruby_2.1.1.sh executable by all so works in RHEL 5

* Mon Mar 24 2014 Guy Gershoni <guy@conchus.com> - 1-0.2.1.1
- Initial version of the package
