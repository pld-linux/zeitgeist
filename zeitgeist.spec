Summary:	Framework providing Desktop activity awareness
Summary(pl.UTF-8):	Szkielet zapewniający świadomość aktywności w środowisku graficznym
Name:		zeitgeist
Version:	0.9.13
Release:	1
License:	LGPL v2.1+
Group:		Daemons
Source0:	http://launchpad.net/zeitgeist/0.9/%{version}/+download/%{name}-%{version}.tar.xz
# Source0-md5:	796b35e817d59402b41da0d2bc1bcc3a
Patch0:		%{name}-lt.patch
URL:		http://launchpad.net/zeitgeist
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	dee-devel >= 1.0.2
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	json-glib-devel >= 0.14.0
BuildRequires:	libraptor2-rapper
BuildRequires:	python >= 1:2.6
BuildRequires:	python-rdflib >= 3.0.0
BuildRequires:	rpm-pythonprov
BuildRequires:	sqlite3-devel >= 3.7.11
BuildRequires:	telepathy-glib-devel >= 0.18.0
BuildRequires:	vala >= 2:0.18.0
BuildRequires:	vala-telepathy-glib >= 0.18.0
BuildRequires:	xapian-core-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus
Provides:	zeitgeist-datahub = %{version}-%{release}
Obsoletes:	zeitgeist-datahub < 0.9.5-2
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

%package libs
Summary:	Zeitgeist library
Summary(pl.UTF-8):	Biblioteka Zeitgeist
Group:		Libraries
Requires:	glib2 >= 1:2.26.0
Requires:	sqlite3 >= 3.7.11

%description libs
This package provides Zeitgeist library.

%description libs -l pl.UTF-8
Ten pakiet dostarcza bibliotekę Zeitgeist.

%package devel
Summary:	Development files for Zeitgeist library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Zeitgeist
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.26.0

%description devel
This package provides development files for Zeitgeist library.

%description devel -l pl.UTF-8
Ten pakiet dostarcza pliki programistyczne dla biblioteki Zeitgeist.

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

%package -n vala-zeitgeist
Summary:	Zeitgeist API for Vala language
Summary(pl.UTF-8):	API Zeitgeist dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.18.0

%description -n vala-zeitgeist
Zeitgeist API for Vala language.

%description -n vala-zeitgeist -l pl.UTF-8
API Zeitgeist dla języka Vala.

%package -n bash-completion-zeitgeist
Summary:	bash-completion for Zeitgeist
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla Zeitgeist
Group:		Applications/Shells
Requires:	bash-completion

%description -n bash-completion-zeitgeist
This package provides bash-completion for Zeitgeist.

%description -n bash-completion-zeitgeist -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla Zeitgeist.

%prep
%setup -q
%patch0 -p1

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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libzeitgeist-2.0.la
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/zeitgeist/doc

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/zeitgeist-daemon
%attr(755,root,root) %{_bindir}/zeitgeist-datahub
/etc/xdg/autostart/zeitgeist-datahub.desktop
%{_datadir}/dbus-1/services/org.gnome.zeitgeist.service
%dir %{_datadir}/zeitgeist
%{_mandir}/man1/zeitgeist-daemon.1*
%{_mandir}/man1/zeitgeist-datahub.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzeitgeist-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libzeitgeist-2.0.so.0
%{_libdir}/girepository-1.0/Zeitgeist-2.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzeitgeist-2.0.so
%{_includedir}/zeitgeist-2.0
%{_datadir}/gir-1.0/Zeitgeist-2.0.gir
%{_pkgconfigdir}/zeitgeist-2.0.pc

%files -n python-%{name}
%defattr(644,root,root,755)
%{py_sitescriptdir}/zeitgeist
%{_datadir}/zeitgeist/ontology

%files -n vala-zeitgeist
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/zeitgeist-2.0.deps
%{_datadir}/vala/vapi/zeitgeist-2.0.vapi
%{_datadir}/vala/vapi/zeitgeist-datamodel-2.0.vapi

%files -n bash-completion-zeitgeist
%defattr(644,root,root,755)
%{_datadir}/bash-completion/completions/zeitgeist-daemon
