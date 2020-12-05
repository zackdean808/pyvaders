Name:           pyvaders
Version:        1
Release:        1%{?dist}
Summary:        Space Invaders is a classic arcade game from the 1980s. PyInvaders is an implementation of this in python.
License:        MIT
URL:            https://github.com/nixbytes/pyvaders
Source0:        pyvaders-1.1.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:       python3-pygame


%description
Space Invaders is a classic arcade game from the 1980s. PyInvaders is an implementation of this in python. 


Summary:        %{summary}


%prep
%autosetup -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/local/bin/pyvaders/
install -d $RPM_BUILD_ROOT/usr/local/bin/pyvaders/assets/


install assets/alien_enemy.png  $RPM_BUILD_ROOT/usr/local/bin/pyvaders/assets/
install assets/alien.png $RPM_BUILD_ROOT/usr/local/bin/pyvaders/assets
install assets/darkgrey_02.png $RPM_BUILD_ROOT/usr/local/bin/pyvaders/assets/
install assets/DFS-Particle-voyager.mp3 $RPM_BUILD_ROOT/usr/local/bin/pyvaders/assets/
install assets/explosion.wav $RPM_BUILD_ROOT/usr/local/bin/pyvaders/assets/
install assets/laser.png $RPM_BUILD_ROOT/usr/local/bin/pyvaders/assets/
install assets/laser.wav $RPM_BUILD_ROOT/usr/local/bin/pyvaders/assets/
install assets/Monoton-Regular.ttf $RPM_BUILD_ROOT/usr/local/bin/pyvaders/assets/
install assets/Monotro-License $RPM_BUILD_ROOT/usr/local/bin/pyvaders/assets/
install assets/mountains03-1920-x-1080_full.png $RPM_BUILD_ROOT/usr/local/bin/pyvaders/assets/
install assets/mountains03-512-x-256_full.png $RPM_BUILD_ROOT/usr/local/bin/pyvaders/assets/
install assets/space-bg.jpg $RPM_BUILD_ROOT/usr/local/bin/pyvaders/assets/
install __init__.py $RPM_BUILD_ROOT/usr/local/bin/pyvaders/
install main.py $RPM_BUILD_ROOT/usr/local/bin/pyvaders/


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
* Fri Dec  4 19:30:52 EST 2020 Zack Dean <zack.dean@gmail.com>
- 
