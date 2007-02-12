Summary:	Portable lossless data compression library
Summary(de.UTF-8):   Library für die Komprimierung
Summary(pl.UTF-8):   Biblioteka bezstratnej kompresji
Name:		ucl
Version:	1.03
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.oberhumer.com/opensource/ucl/download/%{name}-%{version}.tar.gz
# Source0-md5:	852bd691d8abc75b52053465846fba34
URL:		http://www.oberhumer.com/opensource/ucl/
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UCL is a portable lossless data compression library written in ANSI C.
UCL implements a number of compression algorithms that achieve an
excellent compression ratio while allowing *very* fast decompression.
Decompression requires no additional memory.

%description -l pl.UTF-8
UCL jest przenośną biblioteką do kompresji napisaną w ANSI C. Oferuje
doskonały współczynnik kompresji przy bardzo szybkiej dekompresji.
Dekompresja nie wymaga dodatkowej pamięci.

%package devel
Summary:	header files and libraries for ucl development
Summary(de.UTF-8):   Headerdateien und Libraries für ucl-Entwicklung
Summary(pl.UTF-8):   Pliki nagłówkowe i dokumentacja do ucl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files needed to develop programs that
use these ucl.

%description devel -l de.UTF-8
Dieses Paket enthält die Header-Dateien und Libraries, die zur
Entwicklung von Programmen benötigt werden, die diese ucl einsetzen.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłowkowe i dokumentację potrzebną przy
tworzeniu własnych programów wykorzystujących ucl.

%package static
Summary:	Static library for ucl development
Summary(pl.UTF-8):   Biblioteka statyczna do ucl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the header files and libraries needed to develop
programs that use these ucl.

%description static -l pl.UTF-8
Pakiet ten zawiera bibliotekę statyczną potrzebną przy tworzeniu
własnych programów wykorzystujących ucl.

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

%post	-p /sbin/ldconfig
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
