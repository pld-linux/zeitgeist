Summary:	Framework providing Desktop activity awareness
Name:		zeitgeist
Version:	0.7
Release:	0.1
License:	LGPL v2
Group:		Daemons
Source0:	http://launchpad.net/zeitgeist/0.7/0.7.0/+download/%{name}-%{version}.tar.gz
# Source0-md5:	e183137806e1d3870cbaa19f7ed88d8b
Patch0:		no-rdfpipe.patch
URL:		http://launchpad.net/zeitgeist
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libraptor2-rapper
BuildRequires:	python-rdflib
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
%patch0 -p1

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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/zeitgeist-daemon
%{_datadir}/dbus-1/services/org.gnome.zeitgeist.service
%{_datadir}/zeitgeist
%{_mandir}/man1/zeitgeist-daemon.1*
%{py_sitescriptdir}/zeitgeist
%{_pkgconfigdir}/zeitgeist-daemon.pc
