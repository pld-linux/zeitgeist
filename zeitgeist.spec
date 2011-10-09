Summary:	Framework providing Desktop activity awareness
Name:		zeitgeist
Version:	0.8.2
Release:	1
License:	LGPL v2
Group:		Daemons
Source0:	http://launchpad.net/zeitgeist/0.8/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	589e7de784d21177491780bffd11097d
URL:		http://launchpad.net/zeitgeist
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libraptor2-rapper
BuildRequires:	python-rdflib >= 3.0.0
Requires:	python-dbus
Requires:	python-modules
Requires:	python-modules-sqlite
Requires:	python-pygobject
Requires:	python-pyxdg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zeitgeist is a service which logs the users's activities and events
(files opened, websites visites, conversations hold with other people,
etc.) and makes relevant information available to other applications.
It is able to establish relationships between items based on
similarity and usage patterns.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README 
%attr(755,root,root) %{_bindir}/zeitgeist-daemon
%{_datadir}/dbus-1/services/org.gnome.zeitgeist.service
%{_datadir}/zeitgeist
%{_mandir}/man1/zeitgeist-daemon.1*
%{py_sitescriptdir}/zeitgeist
%{_pkgconfigdir}/zeitgeist-daemon.pc
