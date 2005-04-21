%define		__source	.
%define		libical_makeflags	-s

Summary:	IETF's iCalendar Calendaring and Scheduling protocols.
Name:		libical-sope
Version:	1.0
Release:	0.38
Vendor:		OpenGroupware.org
License:	LGPL

Group:		Development/Libraries
AutoReqProv:	off
Source0:	http://download.opengroupware.org/sources/trunk/%{name}-trunk-latest.tar.gz
#Patch0:
URL:		http://www.softwarestudio.org/libical

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

Requires:	libfoundation
Requires:	libobjc-lf2

#Requires: gnustep-make
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gcc-objc
BuildRequires:	gnustep-make >= 1.10.0
BuildRequires:	libobjc-lf2
BuildRequires:	libobjc-lf2-devel
BuildRequires:	libfoundation-devel
BuildRequires:	libfoundation

%description
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols. (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.

%prep

%setup -q -n libical-sope

# ****************************** build ********************************
%build
%{__source} %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh
./cfg-gnustep.sh
%{__make} %{libical_makeflags} all

# ****************************** install ******************************
%install
rm -rf $RPM_BUILD_ROOT
%{__source} %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh

%{__make} %{libical_makeflags} DESTDIR=${RPM_BUILD_ROOT} \
                          FHS_INSTALL_ROOT=${RPM_BUILD_ROOT}%{_prefix} \
                          install

rm -f ${RPM_BUILD_ROOT}%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/libical.la
rm -f ${RPM_BUILD_ROOT}%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/libical.so.0.0.0
rm -f ${RPM_BUILD_ROOT}%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/libicalss.la
rm -f ${RPM_BUILD_ROOT}%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/libicalss.so.0.0.0
rm -f ${RPM_BUILD_ROOT}%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/libicalvcal.la
rm -f ${RPM_BUILD_ROOT}%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/libicalvcal.so.0.0.0

# ****************************** post *********************************
%post
if [ $1 = 1 ]; then
  if [ -d %{_sysconfdir}/ld.so.conf.d ]; then
    echo "%{_libdir}" > %{_sysconfdir}/ld.so.conf.d/libical-sope.conf
  elif [ ! "`grep '%{_libdir}' %{_sysconfdir}/ld.so.conf`" ]; then
    echo "%{_libdir}" >> %{_sysconfdir}/ld.so.conf
  fi
  /sbin/ldconfig
fi

# ****************************** postun *********************************
%postun
if [ $1 = 0 ]; then
  if [ -e %{_sysconfdir}/ld.so.conf.d/libical-sope.conf ]; then
    rm -f %{_sysconfdir}/ld.so.conf.d/libical-sope.conf
  fi
  /sbin/ldconfig
fi

# ****************************** clean ********************************
%clean
rm -fr ${RPM_BUILD_ROOT}

# ****************************** files ********************************
%files
%defattr(644,root,root,755)
%{_libdir}/GNUstep/System/Library/Headers/gnu-gnu-gnu/ical.h
%{_libdir}/GNUstep/System/Library/Headers/gnu-gnu-gnu/icalss.h
%dir %attr(755,root,root) %{_libdir}/GNUstep/System/Library/Headers/gnu-gnu-gnu/libicalvcal
%{_libdir}/GNUstep/System/Library/Headers/gnu-gnu-gnu/libicalvcal/icalvcal.h
%{_libdir}/GNUstep/System/Library/Headers/gnu-gnu-gnu/libicalvcal/port.h
%{_libdir}/GNUstep/System/Library/Headers/gnu-gnu-gnu/libicalvcal/vcaltmp.h
%{_libdir}/GNUstep/System/Library/Headers/gnu-gnu-gnu/libicalvcal/vcc.h
%{_libdir}/GNUstep/System/Library/Headers/gnu-gnu-gnu/libicalvcal/vobject.h
%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/libical.a
%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/libicalss.a
%{_libdir}/GNUstep/System/Library/Libraries/ix86/linux-gnu/libicalvcal.a


# ********************************* changelog *************************
