%define	major		0
%define libname		%mklibname mimedir %{major}
%define develname	%mklibname mimedir -d

Summary:	MIME Directory Profile library
Name:		libmimedir
Version:	0.5
Release:	%{mkrel 3}
URL:		http://sourceforge.net/projects/libmimedir/
License:	BSD
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Fixes definition of libdir in libmimedir.la - AdamW 2008/06
Patch0:		libmimedir-0.5-libdir.patch
Group:		System/Libraries
BuildRequires:	bison
BuildRequires:	flex
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This library parses MIME Directory Profile which is defined in RFC 2425.

%package -n	%{libname}
Summary:	MIME Directory Profile library
Group:          System/Libraries

%description -n	%{libname}
This library parses MIME Directory Profile which is defined in RFC 2425.

%package -n	%{develname}
Summary:	Development library and headers for the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname mimedir 0 -d}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This library parses MIME Directory Profile which is defined in RFC 2425.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .libdir
perl -pi -e 's/444/644/g' Makefile.in

%build
export CFLAGS="%{optflags} -fPIC"
%configure2_5x
# %make doesn't work
make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
mkdir -p %buildroot{%_libdir,%_includedir}
%makeinstall

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING ChangeLog README
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc COPYING ChangeLog README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la


