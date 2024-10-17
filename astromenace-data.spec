Name:		astromenace-data
Version:	1.2
Release:	%mkrel 1
Summary:	Hardcore 3D space shooter with spaceship upgrade possibilities
Group:		Games/Arcade
License:	GPLv3
URL:		https://www.viewizard.com/
Source0:	http://www.viewizard.com/download/AstroMenaceSourceArt_070928.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	astromenace = %{version}
BuildArch:	noarch

%description
Space is a vast area, an unbounded territory where it seems there is a 
room for everybody, but reversal of fortune put things differently. The 
hordes of hostile creatures crawled out from the dark corners of the
universe, craving to conquer your homeland. Their force is compelling,
their legions are interminable. However, humans didn't give up without
a final showdown and put their best pilot to fight back. These malicious
invaders chose the wrong galaxy to conquer and you are to prove it! 
Go ahead and make alien aggressors regret their insolence.

This package provides game data and English, German and Russian language files.

%package -n %{name}-ru
Summary: Russian localization of the AstroMenace game
Requires: astromenace
Conflicts: %{name}-de

%description -n %{name}-ru
Russian localization of the AstroMenace game

%package -n %{name}-de
Summary: Russian localization of the AstroMenace game
Requires: astromenace
Conflicts: %{name}-ru

%description -n %{name}-de
Russian localization of the AstroMenace game

%prep
%setup -qn AstroMenaceSourceArt

cd Ready\ for\ use\ game\ data/

sed -i 's/\r//' DATA*/SCRIPT/*
chmod -x DATA*/SCRIPT/*
sed -i 's/\r//' ReadMe.txt

%build
#nothing to build

%install
rm -rf %{buildroot}

cd Ready\ for\ use\ game\ data/

mkdir -p %{buildroot}%{_datadir}/astromenace
install -m 644 gamedata.vfs %{buildroot}%{_datadir}/astromenace
cp -ra DATA* %{buildroot}%{_datadir}/astromenace
install -m 644 gamelang_en.vfs %{buildroot}%{_datadir}/astromenace
install -m 644 gamelang_de.vfs %{buildroot}%{_datadir}/astromenace
install -m 644 gamelang_ru.vfs %{buildroot}%{_datadir}/astromenace

%clean
rm -rf %{buildroot}

%post -n %{name}-ru
if [ -f %{_datadir}/astromenace/DATA/SCRIPT/text.xml ]; then
    rm -f %{_datadir}/astromenace/DATA/SCRIPT/text.xml
fi
if [ -f %{_datadir}/astromenace/gamelang.vfs ]; then
    rm -f %{_datadir}/astromenace/gamelang.vfs
fi
cd %{_datadir}/astromenace/DATA/SCRIPT/
ln -s ../../DATA_RU/SCRIPT/text_ru.xml text.xml
cd %{_datadir}/astromenace/
ln -s gamelang_ru.vfs gamelang.vfs

%preun -n %{name}-ru
rm -f %{_datadir}/astromenace/DATA/SCRIPT/text.xml
rm -f %{_datadir}/astromenace/gamelang.vfs


%post -n %{name}-de
if [ -f %{_datadir}/astromenace/DATA/SCRIPT/text.xml ]; then
    rm -f %{_datadir}/astromenace/DATA/SCRIPT/text.xml
fi
if [ -f %{_datadir}/astromenace/gamelang.vfs ]; then
    rm -f %{_datadir}/astromenace/gamelang.vfs
fi
cd %{_datadir}/astromenace/DATA/SCRIPT/
ln -s ../../DATA_DE/SCRIPT/text_de.xml text.xml
cd %{_datadir}/astromenace/
ln -s gamelang_de.vfs gamelang.vfs


%preun -n %{name}-de
rm -f %{_datadir}/astromenace/DATA/SCRIPT/text.xml
rm -f %{_datadir}/astromenace/gamelang.vfs

%files
%defattr(-,root,root)
%doc Ready\ for\ use\ game\ data/ReadMe.txt
%{_datadir}/astromenace/DATA/SCRIPT/mis*.xml
%{_datadir}/astromenace/DATA/SCRIPT/PoizAI.xml
%{_datadir}/astromenace/DATA/SCRIPT/aimode.xml
%{_datadir}/astromenace/DATA/SCRIPT/list.xml
%{_datadir}/astromenace/DATA/SCRIPT/my_aimode_7.xml
%{_datadir}/astromenace/DATA_BASE
%{_datadir}/astromenace/DATA_EN
%{_datadir}/astromenace/gamedata.vfs
%{_datadir}/astromenace/gamelang_en.vfs

%files -n %{name}-ru
%defattr(-,root,root)
%{_datadir}/astromenace/DATA_RU
%{_datadir}/astromenace/gamelang_ru.vfs

%files -n %{name}-de
%defattr(-,root,root)
%{_datadir}/astromenace/DATA_DE
%{_datadir}/astromenace/gamelang_de.vfs



%changelog
* Mon Sep 26 2011 Andrey Bondrov <abondrov@mandriva.org> 1.2-1mdv2011.0
+ Revision: 701342
- imported package astromenace-data


* Mon Sep 26 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 1.2-1mdv2010.2
- Spec cleanup

* Sat Nov 21 2009 Andrey Bondrov <bondrov@math.dvgu.ru> 1.2-1mib2009.1
- First build for MIB users
- Mandriva Italia Backports
