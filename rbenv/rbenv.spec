%global rubies_path %{_datarootdir}/rubies
%global system_profile_directory %{_sysconfdir}/profile.d
%global profile_rbenv_script_filename %{system_profile_directory}/%{name}.sh

Name:     	   rbenv
Version:  	   1.1.1
Release:       2%{?dist}
Group: 	  	   Applications/System
Summary:  	   The rbenv program for running multiple Ruby instances.
#BuildArch: 	   noarch
License:  	   MIT
URL:      	   https://github.com/rbenv/rbenv
Source0: 	     %{url}/archive/v%{version}.tar.gz

BuildRequires: bash
#BuildRequires:	hardlink

%description
Installs rbenv in shared location for all users to use. Install rbenv-ruby
packages with ruby versions you want.

%prep
%setup

%build
# Compile dynamic bash extension to speed up rbenv.
src/configure
%make_build -C src
#make -C src

%check
#export PATH="%{buildroot}/%{_bindir}:%{rubies_path}/bin:%{rubies_path}/shims:\$PATH"
#eval "\$(rbenv init -)"
#type rbenv

%install
#%{__mkdir} -p %{buildroot}/%{_pkgdocdir}
#%{__mv} README.md LICENSE %{buildroot}/%{_pkgdocdir}

#%{_sbindir}/hardlink -cvf %{buildroot}/%{_pkgdocdir}
%{__rm} -rf src
%{__rm} -f .agignore .gitignore .vimrc .travis.yml
%{__mkdir} -p %{buildroot}/%{rubies_path}
%{__mkdir} -p %{buildroot}/%{rubies_path}/shims
%{__mkdir} -p %{buildroot}/%{rubies_path}/versions
%{__mkdir} -p %{buildroot}/%{_pkgdocdir}
%{__mv} LICENSE README.md %{buildroot}/%{_pkgdocdir}
%{__mkdir} -p %{buildroot}/%{_datarootdir}/%{name}
%{__mv} * %{buildroot}/%{_datarootdir}/%{name}

%{__mkdir} -p %{buildroot}/%{_bindir}
pushd %{buildroot}/%{_bindir}
ln -s %{_datarootdir}/%{name}/bin/%{name} .
popd

%{__mkdir} -p %{buildroot}/%{system_profile_directory}

echo '%{buildroot}/%{profile_rbenv_script_filename}'
cat > %{buildroot}/%{profile_rbenv_script_filename} <<END_OF_RBENV_PROFILE
#!/bin/bash
# rbenv path update and initialization
#
export PATH="%{rubies_path}/bin:%{rubies_path}/shims:\$PATH"
eval "\$(rbenv init -)"
export RBENV_ROOT=%{rubies_path}
END_OF_RBENV_PROFILE
chmod a+x %{buildroot}/%{profile_rbenv_script_filename}

%post
echo " "
echo "rbenv is installed in %{rubies_path}. Please install rbenv-ruby packages you need and tell rbenv which version to use."

%files
%doc %dir %{_pkgdocdir}
%dir %{rubies_path}/shims
%dir %{rubies_path}/versions
%dir %{rubies_path}
%{_datarootdir}/%{name}
%license %{_pkgdocdir}/LICENSE
%{_pkgdocdir}/README.md
%{_bindir}/%{name}
%{profile_rbenv_script_filename}
#%doc %{_pkgdocdir}
#%{_datarootdir}/%{name}

%changelog
* Fri Jun 23 2017 Ronald Tse <ronald.tse@ribose.com> - 1.1.1
- Update to 1.1.1.

* Sat Feb 27 2016 Jason Miller <nocturnalwarz@gmail.com> - 1.1.0-1
- Making rbenv not a symlink in /opt to better support updating rbenv versions
  without having to reinstall or copy ruby builds

* Mon Mar 31 2014 Guy Gershoni <guy@conchus.com> - 0.4.0-2.1
- Making /etc/profile.d/rbenv.sh executable by all so works in RHEL 5

* Wed Mar 19 2014 Guy Gershoni <guy@conchus.com> - 1-0.4.0
- Initial version of the package

