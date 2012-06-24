Summary:	Portable lossless data compression library
Summary(de):	Library f�r die Komprimierung
Summary(pl):	Biblioteka bezstratnej kompresji
Name:		ucl
Version:	1.03
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.oberhumer.com/opensource/ucl/download/%{name}-%{version}.tar.gz
# Source0-md5:	852bd691d8abc75b52053465846fba34
URL:		http://www.oberhumer.com/opensource/ucl/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UCL is a portable lossless data compression library written in ANSI C.
UCL implements a number of compression algorithms that achieve an
excellent compression ratio while allowing *very* fast decompression.
Decompression requires no additional memory.

%description -l pl
UCL jest przeno�n� bibliotek� do kompresji napisan� w ANSI C. Oferuje
doskona�y wsp�czynnik kompresji przy bardzo szybkiej dekompresji.
Dekompresja nie wymaga dodatkowej pami�ci.

%package devel
Summary:	header files and libraries for ucl development
Summary(de):	Headerdateien und Libraries f�r ucl-Entwicklung
Summary(pl):	Pliki nag��wkowe i dokumentacja do ucl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files needed to develop programs that
use these ucl.

%description devel -l de
Dieses Paket enth�lt die Header-Dateien und Libraries, die zur
Entwicklung von Programmen ben�tigt werden, die diese ucl einsetzen.

%description devel -l pl
Pakiet ten zawiera pliki nag�owkowe i dokumentacj� potrzebn� przy
tworzeniu w�asnych program�w wykorzystuj�cych ucl.

%package static
Summary:	Static library for ucl development
Summary(pl):	Biblioteka statyczna do ucl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the header files and libraries needed to develop
programs that use these ucl.

%description static -l pl
Pakiet ten zawiera bibliotek� statyczn� potrzebn� przy tworzeniu
w�asnych program�w wykorzystuj�cych ucl.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub acconfig
%configure \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/ucl

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
