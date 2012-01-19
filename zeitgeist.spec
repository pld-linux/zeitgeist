Summary:	Framework providing Desktop activity awareness
Summary(pl.UTF-8):	Szkielet zapewniający świadomość aktywności w środowisku graficznym
Name:		zeitgeist
Version:	0.8.2
Release:	3
License:	LGPL v2.1+
Group:		Daemons
Source0:	http://launchpad.net/zeitgeist/0.8/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	589e7de784d21177491780bffd11097d
URL:		http://launchpad.net/zeitgeist
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libraptor2-rapper
BuildRequires:	python >= 1:2.6
BuildRequires:	python-rdflib >= 3.0.0
BuildRequires:	rpm-pythonprov
Requires:	python-%{name} = %{version}-%{release}
Requires:	python-modules-sqlite
Requires:	python-pygobject >= 2.16.0
Requires:	python-pyxdg
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
%doc AUTHORS COPYRIGHT ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/zeitgeist-daemon
%{_datadir}/dbus-1/services/org.gnome.zeitgeist.service
%{_datadir}/zeitgeist/_zeitgeist
%{_mandir}/man1/zeitgeist-daemon.1*
# -devel? (for daemon extensions development)
%{_pkgconfigdir}/zeitgeist-daemon.pc

%files -n python-%{name}
%defattr(644,root,root,755)
%{py_sitescriptdir}/zeitgeist
%dir %{_datadir}/zeitgeist
%{_datadir}/zeitgeist/ontology
