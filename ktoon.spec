%define	name	ktoon
%define	version	0.8.1
%define	release	%mkrel 3
%define	Summary	2D Animation Toolkit

Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Graphics
Summary:	%{Summary}
Source0:	%{name}-%{version}.tar.gz
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch1:		31_dirs.patch
Patch2:		60_daction_q_object.patch
Patch3:		80_fix_build_on_unix.patch
Patch4:		ktoon-0.8.1-fix-desktop.patch
License:	GPLv2+
URL:		http://ktoon.toonka.com/
BuildRequires:	qt4-devel >= 4.1.4
BuildRequires:  MesaGLU-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gstreamer0.10-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
KToon is a 2D Animation Toolkit designed by animators (Toonka Films ) for
animators, focused to the Cartoon\'s industry.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0

%build
./configure
%qmake_qt4
make

%install
rm -rf %buildroot
make install INSTALL_ROOT=%buildroot%_prefix

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor='' \
	--dir %buildroot%_datadir/applications/ \
	%name.desktop

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

mkdir -p %buildroot%_datadir/%name
mv %buildroot%_prefix/plugins %buildroot%_datadir/%name
mv %buildroot%_prefix/data %buildroot%_datadir/%name
mv %buildroot%_prefix/themes %buildroot%_datadir/%name

%if "%_lib" == "lib64"
mkdir -p %buildroot%_libdir
mv %buildroot%_prefix/lib/* %buildroot%_libdir/
%endif

# we do not ship devel files for now
rm -f %buildroot%_libdir/*.so
rm -fr %buildroot%_includedir

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changelog TODO
%{_bindir}/%{name}
%{_libdir}/*.so*
%{_datadir}/%name
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
