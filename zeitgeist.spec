Summary:	Framework providing Desktop activity awareness
Summary(pl.UTF-8):	Szkielet zapewniający świadomość aktywności w środowisku graficznym
Name:		zeitgeist
Version:	0.9.5
Release:	3
License:	LGPL v2.1+
Group:		Daemons
Source0:	http://launchpad.net/zeitgeist/0.9/%{version}/+download/%{name}-%{version}.tar.bz2
# Source0-md5:	5841e4624b07ba74866fb177f1c9aae7
URL:		http://launchpad.net/zeitgeist
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-common
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libraptor2-rapper
BuildRequires:	python >= 1:2.6
BuildRequires:	python-rdflib >= 3.0.0
BuildRequires:	rpm-pythonprov
BuildRequires:	sqlite3-devel >= 3.7
# not required in releases
#BuildRequires:	vala >= 0.16.0
BuildRequires:	xapian-core-devel
Requires:	glib2 >= 1:2.26.0
Requires:	python-%{name} = %{version}-%{release}
Requires:	python-modules-sqlite
Requires:	python-pygobject >= 2.16.0
Requires:	python-pyxdg
Requires:	sqlite3 >= 3.7
Suggests:	zeitgeist-datahub
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zeitgeist is a service which logs the users' activities and events
(files opened, websites visites, conversations hold with other people,
etc.) and makes relevant information available to other applications.
It is able to establish relationships between items based on
similarity and usage patterns.

%description -l pl.UTF-8
Zeitgeist to usługa logująca aktywność użytkowników oraz powiązane
zdarzenia (otwierane pliki, odwiedzane serwisy WWW, rozmowy z innymi
osobami itp.) i udostępniająca informacje o nich innym aplikacjom.
Potrafi ustalić powiązania między elementami w oparciu o podobieństwo
i wzorce użycia.

%package -n python-%{name}
Summary:	Python client library for Zeitgeist DBus API
Summary(pl.UTF-8):	Biblioteka kliencka w Pythonie do DBus API demona Zeitgeist
Group:		Development/Languages/Python
Requires:	python-dbus
Requires:	python-modules
Conflicts:	zeitgeist < 0.8.2-2

%description -n python-%{name}
Python client library for Zeitgeist DBus API.

%description -n python-%{name} -l pl.UTF-8
Biblioteka kliencka w Pythonie do DBus API demona Zeitgeist.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-fts \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/zeitgeist-daemon
%{_datadir}/dbus-1/services/org.gnome.zeitgeist.service
%dir %{_datadir}/zeitgeist
%{_mandir}/man1/zeitgeist-daemon.1*

%files -n python-%{name}
%defattr(644,root,root,755)
%{py_sitescriptdir}/zeitgeist
%{_datadir}/zeitgeist/ontology
