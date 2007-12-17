%define	name	libmimedir
%define	version	0.5
%define	release	%mkrel 1
%define	major	0
%define libname	%mklibname mimedir %{major}

Summary:	MIME Directory Profile library
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://sourceforge.net/projects/libmimedir/
License:	BSD
Source0:	%{name}-%{version}.tar.bz2
Group:		System/Libraries
BuildRequires:	bison
BuildRequires:	flex

%description
This library parses MIME Directory Profile which is defined in RFC 2425.

%package -n	%{libname}
Summary:	MIME Directory Profile library
Group:          System/Libraries
Obsoletes:	%{name} < %{version}-%{release}
Provides:	%{libname} = %{version}-%{release}

%description -n	%{libname}
This library parses MIME Directory Profile which is defined in RFC 2425.

%package -n	%{libname}-devel
Summary:	Development library and header files for the %{name} library
Group:		Development/C
Obsoletes:	%{name}-devel < %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libname}-devel
This library parses MIME Directory Profile which is defined in RFC 2425.

%prep

%setup -q -n %{name}-%{version}

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

%files -n %{libname}-devel
%defattr(-,root,root)
%doc COPYING ChangeLog README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la


