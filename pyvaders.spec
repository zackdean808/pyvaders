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


Requires:	python3-pygame

%prep
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}
cp -rp * %{buildroot}


%check

%files
%attr(0744, root, root) 
/usr/local/bin/pyvaders/assets/alien_enemy.png
/usr/local/bin/pyvaders/assets/alien.png
/usr/local/bin/pyvaders/assets/darkgrey_02.png
/usr/local/bin/pyvaders/assets/explosion.wav
/usr/local/bin/pyvaders/assets/laser.png
/usr/local/bin/pyvaders/assets/laser.wav
/usr/local/bin/pyvaders/assets/Monoton-Regular.ttf
/usr/local/bin/pyvaders/assets/Monotro-License
/usr/local/bin/pyvaders/assets/mountains03-1920-x-1080_full.png
/usr/local/bin/pyvaders/assets/mountains03-512-x-256_full.png
/usr/local/bin/pyvaders/assets/space-bg.jpg
/usr/local/bin/pyvaders/__init__.py
/usr/local/bin/pyvaders/main.py


%changelog
* Wed Dec  2 20:00:08 EST 2020 z
- 
