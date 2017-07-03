%global gitdate 20170703
%global commit0 61ba51bcf0b2c1b0d2b3a27b4c24d71b82ff579d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           thunar-dropbox
Version:	0.2.1
Release:    	3%{?gver}%{dist}
License:	GPLv3
Summary:	Plugin for thunar that adds context-menu items for dropbox.
Url:		http://www.softwarebakery.com/maato/thunar-dropbox.html
Group:		System/GUI/Other
Source0: 	https://github.com/Maato/thunar-dropbox/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:	python2-devel
BuildRequires:  python-setuptools
BuildRequires:  binutils
BuildRequires: 	Thunar-devel
BuildRequires:	waf

Requires: hicolor-icon-theme
Requires: Thunar
Requires: dropbox

%description
Plugin for thunar that adds context-menu items for dropbox. 

%prep
%autosetup -n %{name}-%{commit0}

%ifarch x86_64
sed -i 's|${PREFIX}/lib|${PREFIX}/lib64|g' wscript
%endif

%build
python2 waf configure --prefix=/usr  
python2 waf build 

%install
python2 waf install --destdir=%{buildroot}

%post
gtk-update-icon-cache %{_datadir}/icons/hicolor/

%postun 
gtk-update-icon-cache %{_datadir}/icons/hicolor/

%files
%{_libdir}/thunarx-2/thunar-dropbox.so 
%{_datadir}/icons/hicolor/16x16/apps/thunar-dropbox.png


%changelog

* Mon Jul 03 2017 David Vasquez <davidjeremias82 at gmail dot com> 0.2.1-3.git61ba51b
- Updated to 0.2.1-3.git61ba51b

* Wed Apr 22 2015 <davidjeremias82 AT gmail DOT com> 0.2.1-1
- Updated to 0.2.1

* Sun Dec 14 2014 David Vasquez <davidjeremias82 AT gmail DOT com> - 0.2.0-1
- Initial package.
