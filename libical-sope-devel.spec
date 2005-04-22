# TODO:
# - spec filename vs Name
# - what about shared libs?

%define		libical_makeflags	-s

Summary:	IETF's iCalendar Calendaring and Scheduling protocols
Summary(pl):	Protoko³y kalendarza i planowania IETF iCalendar
Name:		libical-sope
Version:	1.0
Release:	0.38
Vendor:		OpenGroupware.org
License:	LGPL
Group:		Development/Libraries
Source0:	http://download.opengroupware.org/sources/trunk/%{name}-trunk-latest.tar.gz
#Patch0:
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
# should be autodetected
#Requires:	gnustep-make
#Requires:	libfoundation
#Requires:	libobjc-lf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols. (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.

%description -l pl
Libical to implementacja z otwartymi ¼ród³ami protoko³ów kalendarza i
planowania IETF iCalendar (RFC 2445, 2446 i 2447). Przetwarza
sk³adniki iCal i udostêpnia API C do obróbki w³a¶ciwo¶ci, parametrów i
podelementów sk³adników iCal.

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
