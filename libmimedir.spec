%define	major		0
%define libname		%mklibname mimedir %{major}
%define develname	%mklibname mimedir -d

Summary:	MIME Directory Profile library
Name:		libmimedir
Version:	0.5.1
Release:	%mkrel 2
URL:		http://sourceforge.net/projects/libmimedir/
License:	BSD
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
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

find %buildroot -name *.so* -exec chmod 755 {} \;

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

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


