%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Name:		gnome-klotski
Version:	3.34.0
Release:	1
Summary:	GNOME Klotski game
License:	GPLv2+ and GFDL
Group:		Games/Puzzles
URL:		https://wiki.gnome.org/Klotski
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:	meson
BuildRequires:	vala-devel
BuildRequires:	librsvg-vala-devel
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(libgnome-games-support-1)
Obsoletes:	gnotski
# For help
Requires:	yelp

%description
A series of sliding block puzzles. Try and solve them in the least number of
moves.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/applications/org.gnome.Klotski.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/org.gnome.Klotski.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Klotski.gschema.xml
