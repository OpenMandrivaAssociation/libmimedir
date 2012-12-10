%define	major		0
%define libname		%mklibname mimedir %{major}
%define develname	%mklibname mimedir -d

Summary:	MIME Directory Profile library
Name:		libmimedir
Version:	0.5.1
Release:	4
URL:		http://sourceforge.net/projects/libmimedir/
License:	BSD
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Group:		System/Libraries
BuildRequires:	bison
BuildRequires:	flex

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
mkdir -p %buildroot{%_libdir,%_includedir}
%makeinstall

find %buildroot -name *.so* -exec chmod 755 {} \;

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




%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-3mdv2011.0
+ Revision: 609757
- rebuild

* Thu Apr 29 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.5.1-2mdv2010.1
+ Revision: 540950
- fix .so permissions so that debug info are extracted

* Tue Jun 09 2009 Götz Waschk <waschk@mandriva.org> 0.5.1-1mdv2010.0
+ Revision: 384225
- new version
- drop patch

* Fri Jun 05 2009 Götz Waschk <waschk@mandriva.org> 0.5-4mdv2010.0
+ Revision: 382952
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jun 03 2008 Adam Williamson <awilliamson@mandriva.org> 0.5-3mdv2009.0
+ Revision: 214699
- new devel policy
- clean spec
- better fix for the libdir issue (found where it was broken and patched it)

* Tue Jun 03 2008 Adam Williamson <awilliamson@mandriva.org> 0.5-2mdv2009.0
+ Revision: 214481
- hacky fix for an incorrect libdir line in .la file which is breaking builds way up the line

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.5-1mdv2008.1
+ Revision: 140925
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Nov 30 2006 Olivier Thauvin <nanardon@mandriva.org> 0.5-1mdv2007.0
+ Revision: 89462
- don't use make -j, doesn't work
- reimport package
- Create libmimedir

* Thu Jun 03 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.3-1mdk
- initial cooker contrib

