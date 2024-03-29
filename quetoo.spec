# TODO:
# - R some quake2-data package: Data: /usr/share/quake2
Summary:	Quetoo: quetoo for deathmatch haX0rs
Summary(pl.UTF-8):	Quetoo: quetoo dla haX0rów trybu deathmatch
Name:		quetoo
Version:	0.6.1
Release:	0.1
License:	GPL v2
Group:		Applications/Games
Source0:	http://tastyspleen.net/~jdolan/%{name}-%{version}.tar.bz2
# Source0-md5:	2255c1d9857c725f6e82662593fcb51e
URL:		http://jdolan.dyndns.org/trac/wiki/Quetoo
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamelibdir	%{_libdir}/quetoo
%define		_gamedatadir	%{_datadir}/quetoo
%define		_gamehomedir	/var/games/quetoo

%description
This is a source port of id Software's Quake II. Initially a fork of
the Quake2Forge project, this engine aims to provide security and
performance enhancements. If you're looking for visual effect updates
and gimmick features, run something else...

%description -l pl.UTF-8
Jest to port źródeł gry Quake II firmy id Software. Silnik ten,
początkowo będący odgałęzieniem projektu Quake2Forge, ma na celu
zapewnienie rozszerzenia bezpieczeństwa i wydajności. Nie należy się
spodziewać uaktualnień efektów wizualnych czy nowych, zaskakujących
możliwości.

%prep
%setup -q
%{__sed} -i -e '
	# those games are missing in tarball
    /data\/ctf/d
    /data\/qmass/d
    /data\/vanctf/d

    /src\/ctf/d
    /src\/qmass/d
    /src\/vanctf/d
' configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-warn \
	--disable-static \
	--with-opengl \
	--with-sdl \
	--with-zlib \
	--with-mysql \
	--with-games='baseq2'

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/baseq2/game.la



%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/quetoo
%{_libdir}/%{name}/baseq2/game.so
