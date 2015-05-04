%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-klotski
Version:	3.16.1
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
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Tue Feb 17 2015 wally <wally> 3.14.2-2.mga5
+ Revision: 815338
- require yelp for showing help

* Tue Nov 11 2014 ovitters <ovitters> 3.14.2-1.mga5
+ Revision: 796297
- new version 3.14.2

* Wed Oct 15 2014 umeabot <umeabot> 3.14.1-2.mga5
+ Revision: 746015
- Second Mageia 5 Mass Rebuild

* Fri Oct 10 2014 ovitters <ovitters> 3.14.1-1.mga5
+ Revision: 737812
- new version 3.14.1

* Mon Sep 22 2014 ovitters <ovitters> 3.14.0-1.mga5
+ Revision: 719182
- new version 3.14.0

* Tue Sep 16 2014 umeabot <umeabot> 3.13.90-2.mga5
+ Revision: 679729
- Mageia 5 Mass Rebuild

* Tue Aug 19 2014 ovitters <ovitters> 3.13.90-1.mga5
+ Revision: 665325
- new version 3.13.90

* Tue Jun 24 2014 ovitters <ovitters> 3.13.3-1.mga5
+ Revision: 639208
- new version 3.13.3

* Mon May 12 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 622336
- new version 3.12.2

* Mon Apr 14 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 614155
- new version 3.12.1

* Mon Mar 24 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 608068
- new version 3.12.0

* Mon Mar 17 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604566
- new version 3.11.92

* Tue Feb 18 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 594255
- new version 3.11.90

* Wed Feb 05 2014 dams <dams> 3.11.3-1.mga5
+ Revision: 583008
- new version 3.11.3

* Sat Nov 09 2013 ovitters <ovitters> 3.10.0-3.mga4
+ Revision: 550162
- fix url

* Sat Oct 19 2013 umeabot <umeabot> 3.10.0-2.mga4
+ Revision: 536538
- Mageia 4 Mass Rebuild

* Mon Sep 23 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 484537
- new version 3.10.0

* Tue Sep 17 2013 ovitters <ovitters> 3.9.92-1.mga4
+ Revision: 480578
- new version 3.9.92

* Wed Aug 21 2013 fwang <fwang> 3.9.90-1.mga4
+ Revision: 468754
- new version 3.9.90
- cleanup spec

* Sun Jun 09 2013 dams <dams> 3.8.2-1.mga4
+ Revision: 440914
- imported package gnome-klotski

