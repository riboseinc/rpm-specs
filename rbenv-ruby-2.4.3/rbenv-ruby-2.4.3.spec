%global major_version 2
%global minor_version 4
%global teeny_version 3
%global major_minor_version %{major_version}.%{minor_version}
%global ruby_version %{major_minor_version}.%{teeny_version}
%global ruby_release %{ruby_version}
%global ruby_name ruby

%global ruby_archive %{ruby_name}-%{ruby_version}
#%#global revision 58214

# If revision and milestone are removed/commented out, the official release
# build is expected.
%if 0%{?milestone:1}%{?revision:1} != 0
%global development_release %{?milestone}%{?!milestone:%{?revision:r%{revision}}}
%global ruby_archive %{ruby_archive}-%{?milestone}%{?!milestone:%{?revision:r%{revision}}}
%endif

%global release 1
%{!?release_string:%global release_string %{?development_release:0.}%{release}%{?development_release:.%{development_release}}%{?dist}}

%global rubies_path %{_datarootdir}/rubies
%global ruby_instance_path %{rubies_path}/versions/%{ruby_version}

Name:          rbenv-%{ruby_archive}
Version:       %{ruby_version}
Release:       %{release_string}
#Release:       1%{?dist}
Group:         Development/Languages
Summary:       A ruby instance that can co-exist with other instances in the rbenv (RPM) ecosystem.
License:       MIT
URL:           http://ruby-lang.org/

BuildRequires: redhat-rpm-config ruby-build rbenv

# For running rubies
Requires: openssl libyaml rbenv

%description
Installs %{name}

%prep

%build
. /etc/profile.d/rbenv.sh
rbenv install %{ruby_version}

%install
%{__mkdir} -p %{buildroot}/%{rubies_path}/versions
%{__mv} %{ruby_instance_path} %{buildroot}/%{ruby_instance_path}

%post
rbenv rehash

%files
%dir %{ruby_instance_path}
%doc %{ruby_instance_path}/share
#%{_bindir}/*
#%{_datarootdir}/%{name}
%{ruby_instance_path}/bin
%{ruby_instance_path}/include
%{ruby_instance_path}/lib

#%license %{_pkgdocdir}/LICENSE

%changelog
* Wed Jan 24 2018 Jeffrey Lau <jeffrey.lau@ribose.com> - 2.4.3-1
- Fix release string

* Mon Jan 22 2018 Jeffrey Lau <jeffrey.lau@ribose.com> - 2.4.3
- Initial commit

