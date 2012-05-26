#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	static_libs	# don't build static libraries
#
Summary:	GObject RSS handling library
Name:		libgrss
Version:	0.5.0
Release:	1
License:	LGPL v3
Group:		Libraries
Source0:	http://gtk.mplat.es/libgrss/tarballs/%{name}-%{version}.tar.gz
# Source0-md5:	1a91770f5c5a77eb33f72dc7c33f876d
URL:		http://live.gnome.org/Libgrss
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.10
BuildRequires:	glib2-devel >= 1:2.22.2
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	libsoup-devel >= 2.28.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.7.4
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgrss is a GLib abstraction to handle feeds in RSS, Atom and other
formats.

%package devel
Summary:	Header files for grss library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki grss
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.22.2
Requires:	libsoup-devel >= 2.28.1
Requires:	libxml2-devel >= 1:2.7.4

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

%description apidocs
grss library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki grss.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{__enable_disable apidocs gtk-doc} \
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
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_libdir}/libgrss-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgrss-1.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgrss-1.0.so
%{_includedir}/libgrss
%{_pkgconfigdir}/libgrss-0.5.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgrss-1.0.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgrss
%endif
