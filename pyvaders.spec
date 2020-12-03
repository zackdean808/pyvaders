%{?!python3_pkgversion:%global python3_pkgversion 3}

%global %pypi_name ...

Name:           pyvaders
Version:	1         
Release:        1%{?dist}
Summary:        Space Invaders is a classic arcade game from the 1980s. PyInvaders is an implementation of this in python. 
License:        MIT
URL:            https://github.com/nixbytes/pyvaders
Source0:        pyvaders-1.1.tar.gz

BuildArch:      noarch 

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
Space Invaders is a classic arcade game from the 1980s. PyInvaders is an implementation of this in python


%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:	python3-pygame

%description -n python%{python3_pkgversion}-%{pypi_name}


%prep
%autosetup -p1


%build
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
%py3_install


%check
# use what your upstream is using
%{__python3} setup.py test
%{__python3} -m pytest
%{__python3} -m nose
...


%files -n  python%{python3_pkgversion}-%{pypi_name}
%license add-license-file-here
%doc add-docs-here
# For noarch packages: sitelib
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
# For arch-specific packages: sitearch
%{python3_sitearch}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/


%changelog
* Wed Dec  2 20:00:08 EST 2020 z
- 
