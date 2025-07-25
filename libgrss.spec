#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	static_libs	# don't build static libraries

Summary:	GObject RSS handling library
Summary(pl.UTF-8):	Biblioteka GObject do obsługi RSS
Name:		libgrss
Version:	0.7.0
Release:	3
License:	LGPL v3+
Group:		Libraries
Source0:	https://download.gnome.org/sources/libgrss/0.7/%{name}-%{version}.tar.xz
# Source0-md5:	7c0ee46a82dc0e9610183fe9ef8c7c1d
URL:		https://wiki.gnome.org/Projects/Libgrss
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.42.1
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	libsoup-devel >= 2.48.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 1:2.9.2
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.42.1
Requires:	libsoup >= 2.48.0
Requires:	libxml2 >= 1:2.9.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgrss is a GLib abstraction to handle feeds in RSS, Atom and other
formats.

%description -l pl.UTF-8
libgrss to abstrakcja GLiba do obsługi danych w formatach RSS, Atom i
innych.

%package devel
Summary:	Header files for grss library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki grss
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.42.1
Requires:	libsoup-devel >= 2.48.0
Requires:	libxml2-devel >= 1:2.9.2

%description devel
Header files for grss library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki grss.

%package static
Summary:	Static grss library
Summary(pl.UTF-8):	Statyczna biblioteka grss
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static grss library.

%description static -l pl.UTF-8
Statyczna biblioteka grss.

%package apidocs
Summary:	grss library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki grss
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
grss library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki grss.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{__enable_disable apidocs gtk-doc} \
	--disable-silent-rules \
	%{__enable_disable static_libs static} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libgrss.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgrss.so.0
%{_libdir}/girepository-1.0/Grss-0.7.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgrss.so
%{_includedir}/libgrss
%{_datadir}/gir-1.0/Grss-0.7.gir
%{_pkgconfigdir}/libgrss.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgrss.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgrss
%endif
