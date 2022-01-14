Summary:	Framework providing Desktop activity awareness
Summary(pl.UTF-8):	Szkielet zapewniający świadomość aktywności w środowisku graficznym
Name:		zeitgeist
Version:	1.0.4
Release:	1
License:	LGPL v2.1+
Group:		Daemons
Source0:	https://launchpad.net/zeitgeist/1.0/%{version}/+download/%{name}-%{version}.tar.xz
# Source0-md5:	f02e8be3dc5f18a67be3b1272108d584
Patch0:		%{name}-lt.patch
Patch1:		%{name}-vala.patch
URL:		http://launchpad.net/zeitgeist
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.11
BuildRequires:	dbus-devel
BuildRequires:	dee-devel >= 1.0.2
BuildRequires:	gettext-tools >= 0.19
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	json-glib-devel >= 0.14.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig >= 1:0.21
BuildRequires:	python3
BuildRequires:	python3-rdflib >= 3.0.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.682
BuildRequires:	sqlite3-devel >= 3.7.11
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-glib-devel >= 0.18.0
BuildRequires:	vala >= 2:0.32.1
BuildRequires:	vala-telepathy-glib >= 0.18.0
BuildRequires:	valadoc >= 0.2
BuildRequires:	xapian-core-devel
BuildRequires:	xz
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus
Requires:	dee >= 1.0.2
Requires:	json-glib >= 0.14.0
Requires:	telepathy-glib >= 0.18.0
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
Requires:	glib2 >= 1:2.36.0
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
Requires:	glib2-devel >= 1:2.36.0

%description devel
This package provides development files for Zeitgeist library.

%description devel -l pl.UTF-8
Ten pakiet dostarcza pliki programistyczne dla biblioteki Zeitgeist.

%package -n python3-%{name}
Summary:	Python client library for Zeitgeist DBus API
Summary(pl.UTF-8):	Biblioteka kliencka w Pythonie do DBus API demona Zeitgeist
Group:		Development/Languages/Python
Requires:	python3-dbus
Requires:	python3-modules
Obsoletes:	python-zeitgeist < 1.0.3
Conflicts:	zeitgeist < 0.8.2-2
BuildArch:	noarch

%description -n python3-%{name}
Python client library for Zeitgeist DBus API.

%description -n python3-%{name} -l pl.UTF-8
Biblioteka kliencka w Pythonie do DBus API demona Zeitgeist.

%package -n vala-zeitgeist
Summary:	Zeitgeist API for Vala language
Summary(pl.UTF-8):	API Zeitgeist dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.32.1
BuildArch:	noarch

%description -n vala-zeitgeist
Zeitgeist API for Vala language.

%description -n vala-zeitgeist -l pl.UTF-8
API Zeitgeist dla języka Vala.

%package -n bash-completion-zeitgeist
Summary:	bash-completion for Zeitgeist
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla Zeitgeist
Group:		Applications/Shells
Requires:	bash-completion >= 2.0
BuildArch:	noarch

%description -n bash-completion-zeitgeist
This package provides bash-completion for Zeitgeist.

%description -n bash-completion-zeitgeist -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla Zeitgeist.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-fts
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libzeitgeist-2.0.la
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/zeitgeist/doc

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
%dir %{_libexecdir}/%{name}
%attr(755,root,root) %{_libexecdir}/%{name}/zeitgeist-fts
%{_datadir}/dbus-1/services/org.gnome.zeitgeist.Engine.service
%{_datadir}/dbus-1/services/org.gnome.zeitgeist.SimpleIndexer.service
%{_mandir}/man1/zeitgeist-daemon.1*
%{_mandir}/man1/zeitgeist-datahub.1*
%{systemduserunitdir}/zeitgeist.service
%{systemduserunitdir}/zeitgeist-fts.service

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzeitgeist-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libzeitgeist-2.0.so.0
%{_libdir}/girepository-1.0/Zeitgeist-2.0.typelib
%dir %{_datadir}/zeitgeist

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzeitgeist-2.0.so
%{_includedir}/zeitgeist-2.0
%{_datadir}/gir-1.0/Zeitgeist-2.0.gir
%{_pkgconfigdir}/zeitgeist-2.0.pc

%files -n python3-%{name}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/zeitgeist
%{_datadir}/zeitgeist/ontology

%files -n vala-zeitgeist
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/zeitgeist-2.0.deps
%{_datadir}/vala/vapi/zeitgeist-2.0.vapi
%{_datadir}/vala/vapi/zeitgeist-datamodel-2.0.vapi

%files -n bash-completion-zeitgeist
%defattr(644,root,root,755)
%{bash_compdir}/zeitgeist-daemon
