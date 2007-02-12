# TODO:
# - spec filename vs Name
# - what about shared libs?
%define		trunkdata		200410151506
%define		libical_makeflags	-s

Summary:	IETF's iCalendar Calendaring and Scheduling protocols
Summary(pl.UTF-8):   Protokoły kalendarza i planowania IETF iCalendar
Name:		libical-sope
Version:	r55  
Release:	0.1
Vendor:		OpenGroupware.org
License:	LGPL
Group:		Development/Libraries
Source0:	http://download.opengroupware.org/sources/trunk/%{name}-trunk-%{version}-%{trunkdata}.tar.gz
# Source0-md5:	7b81daedbf468ebf796a166ad28473da
URL:		http://www.softwarestudio.org/libical/
#AutoReqProv:	off
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gcc-objc
BuildRequires:	gnustep-make >= 1.10.0
BuildRequires:	libfoundation-devel
BuildRequires:	libobjc-lf2-devel
BuildRequires:	libical-devel
Requires:	gnustep-make
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols. (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.

%description -l pl.UTF-8
Libical to implementacja z otwartymi źródłami protokołów kalendarza i
planowania IETF iCalendar (RFC 2445, 2446 i 2447). Przetwarza
składniki iCal i udostępnia API C do obróbki właściwości, parametrów i
podelementów składników iCal.

%prep
%setup -q -n libical-sope

%build
. %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh
./cfg-gnustep.sh
%{__make} %{libical_makeflags} all

%install
rm -rf $RPM_BUILD_ROOT
. %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh

%{__make} %{libical_makeflags} install \
	DESTDIR=$RPM_BUILD_ROOT \
	FHS_INSTALL_ROOT=$RPM_BUILD_ROOT%{_prefix}

rm -f $RPM_BUILD_ROOT%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/libical.la
rm -f $RPM_BUILD_ROOT%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/libical.so.0.0.0
rm -f $RPM_BUILD_ROOT%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/libicalss.la
rm -f $RPM_BUILD_ROOT%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/libicalss.so.0.0.0
rm -f $RPM_BUILD_ROOT%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/libicalvcal.la
rm -f $RPM_BUILD_ROOT%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/libicalvcal.so.0.0.0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/GNUstep/System/Library/Headers/gnu-gnu-gnu/ical.h
%{_libdir}/GNUstep/System/Library/Headers/gnu-gnu-gnu/icalss.h
%dir %{_libdir}/GNUstep/System/Library/Headers/gnu-gnu-gnu/libicalvcal
%{_libdir}/GNUstep/System/Library/Headers/gnu-gnu-gnu/libicalvcal/icalvcal.h
%{_libdir}/GNUstep/System/Library/Headers/gnu-gnu-gnu/libicalvcal/port.h
%{_libdir}/GNUstep/System/Library/Headers/gnu-gnu-gnu/libicalvcal/vcaltmp.h
%{_libdir}/GNUstep/System/Library/Headers/gnu-gnu-gnu/libicalvcal/vcc.h
%{_libdir}/GNUstep/System/Library/Headers/gnu-gnu-gnu/libicalvcal/vobject.h
%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/libical.a
%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/libicalss.a
%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/libicalvcal.a
