%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Name:		gnome-klotski
Version:	3.22.3
Release:	1
Summary:	GNOME Klotski game
License:	GPLv2+ and GFDL
Group:		Games/Puzzles
URL:		https://wiki.gnome.org/Klotski
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:	intltool
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
%configure
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.klotski.gschema.xml
%{_datadir}/%{name}
%{_iconsdir}/*/*/apps/%{name}.*
%{_iconsdir}/*/*/apps/%{name}-symbolic.*
%{_mandir}/man6/%{name}.6*
%{_datadir}/metainfo/%{name}.appdata.xml

