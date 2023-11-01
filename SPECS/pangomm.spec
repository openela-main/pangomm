%define apiver 1.4
# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

%global glibmm_version 2.48.0
%global cairomm_version 1.2.2
%global pango_version 1.45.1

Name:           pangomm
Version:        2.46.1
Release:        1%{?dist}
Summary:        C++ interface for Pango

License:        LGPLv2+
URL:            https://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/pangomm/%{release_version}/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(cairomm-1.0) >= %{cairomm_version}
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  glibmm24-devel >= %{glibmm_version}
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  mm-common
BuildRequires:  pango-devel >= %{pango_version}

Requires:       glibmm24%{?_isa} >= %{glibmm_version}
Requires:       cairomm1.0%{?_isa} >= %{cairomm_version}
Requires:       pango%{?_isa} >= %{pango_version}

%description
pangomm provides a C++ interface to the Pango library. Highlights
include typesafe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.


%package devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the libraries and header files needed for
developing pangomm applications.


%package          doc
Summary:          Developer's documentation for the pangomm library
BuildArch:        noarch
Requires:         %{name} = %{version}-%{release}
Requires:         libsigc++20-doc
Requires:         glibmm24-doc

%description      doc
This package contains developer's documentation for the pangomm
library. Pangomm is the C++ API for the Pango font layout library.

The documentation can be viewed either through the devhelp
documentation browser or through a web browser.

%prep
%setup -q


%build
%meson -Dbuild-documentation=true
%meson_build


%install
%meson_install


%files
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/libpangomm-%{apiver}.so.1*


%files devel
%{_includedir}/pangomm-%{apiver}
%{_libdir}/libpangomm-%{apiver}.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/pangomm-%{apiver}

%files doc
%doc %{_docdir}/pangomm-%{apiver}/
%{_datadir}/devhelp/

%changelog
* Tue Aug 24 2021 Kalev Lember <klember@redhat.com> - 2.46.1-1
- Update to 2.46.1

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 2.42.2-5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.42.2-4
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Fri Feb 12 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.42.2-3
- Use pkgconfig to BR the required cairomm API/ABI version 1.0 (vs. 1.16); use
  cairomm1.0, which may be a virtual Provides, in the manual lib Requires

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.42.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Kalev Lember <klember@redhat.com> - 2.42.2-1
- Update to 2.42.2
- Update source URLs
- Switch to meson build system
- Tighten soname globs

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.42.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 27 2020 Kalev Lember <klember@redhat.com> - 2.42.1-1
- Update to 2.42.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Kalev Lember <klember@redhat.com> - 2.40.2-1
- Update to 2.40.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 21 2016 Kalev Lember <klember@redhat.com> - 2.40.1-1
- Update to 2.40.1

* Wed Mar 30 2016 Kalev Lember <klember@redhat.com> - 2.40.0-1
- Update to 2.40.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.39.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Kalev Lember <klember@redhat.com> - 2.39.1-1
- Update to 2.39.1

* Tue Sep 22 2015 Kalev Lember <klember@redhat.com> - 2.38.1-1
- Update to 2.38.1
- Use make_install macro
- Set minimum versions for required libraries
- Tighten -devel deps with the _isa macro

* Tue Sep 15 2015 Richard Hughes <rhughes@redhat.com> - 2.37.2-1
- Update to 2.37.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.36.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.36.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 24 2015 Kalev Lember <kalevlember@gmail.com> - 2.36.0-1
- Update to 2.36.0
- Use license macro for the COPYING file
- Drop large ChangeLog file

* Fri Feb 13 2015 Richard Hughes <rhughes@redhat.com> - 2.35.1-1
- Update to 2.35.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.34.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.34.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Kalev Lember <kalevlember@gmail.com> - 2.34.0-1
- Update to 2.34.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 Kalev Lember <kalevlember@gmail.com> - 2.28.4-1
- Update to 2.28.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 2.28.3-1
- Update to 2.28.3

* Thu Mar 31 2011 Kalev Lember <kalev@smartlink.ee> - 2.28.2-1
- Update to 2.28.2

* Fri Mar 25 2011 Kalev Lember <kalev@smartlink.ee> - 2.28.1-1
- Update to 2.28.1
- Removed old obsoletes for gtkmm24

* Wed Mar 02 2011 Kalev Lember <kalev@smartlink.ee> - 2.27.1-3
- Own /usr/share/doc/pangomm-1.4/ dir
- Require base package from -doc subpackage

* Mon Feb 21 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 2.27.1-2
- split doc into subpackage
- fix documentation location
- co-own /usr/share/devhelp

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Kalev Lember <kalev@smartlink.ee> - 2.27.1-1
- Update to 2.27.1
- Use macro for figuring out first two digits of version

* Wed Sep 29 2010 jkeating - 2.26.2-3
- Rebuilt for gcc bug 634757

* Tue Sep 14 2010 Kalev Lember <kalev@smartlink.ee> - 2.26.2-2
- Co-own /usr/share/gtk-doc/ directory (#604407)
- Dropped pkgconfig dep from -devel subpackage which is now automatically added

* Mon Jul 05 2010 Kalev Lember <kalev@smartlink.ee> - 2.26.2-1
- Update to 2.26.2

* Tue Apr 13 2010 Haïkel Guémar <hguemar@fedoraproject.org> -2.26.0-2
- Rebuilt for F-13

* Fri Sep 25 2009 Denis Leroy <denis@poolshark.org> - 2.26.0-1
- Update to upstream 2.26.0

* Mon Sep 14 2009 Denis Leroy <denis@poolshark.org> - 2.25.1.3-1
- Update to upstream 2.25.1.3
- Package pangomm libdir directory with config include header
- Fix documentation location

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr  1 2009 Denis Leroy <denis@poolshark.org> - 2.24.0-1
- Update to upstream 2.24.0

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Denis Leroy <denis@poolshark.org> - 2.14.1-1
- Update to 2.14.1
- Devhelp patch upstreamed

* Sun Oct 12 2008 Denis Leroy <denis@poolshark.org> - 2.14.0-2
- Added patch to fix devhelp main page

* Tue Sep 23 2008 Denis Leroy <denis@poolshark.org> - 2.14.0-1
- Update to stable 2.14.0

* Fri Aug 29 2008 Denis Leroy <denis@poolshark.org> - 2.13.7-3
- Obsoletes older gtkmm to avoid libpangomm conflict 

* Wed Aug 27 2008 Denis Leroy <denis@poolshark.org> - 2.13.7-2
- Spec review fixes

* Mon Aug 25 2008 Denis Leroy <denis@poolshark.org> - 2.13.7-1
- First version
