%define	name	ktoon
%define	version	0.7.3
%define	release	%mkrel 3
%define	Summary	2D Animation Toolkit

Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Graphics
Summary:	%{Summary}
Source0:	%{name}src-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
License:	GPL
URL:		http://ktoon.toonka.com/
BuildRequires:	qt3-devel
BuildRequires:  MesaGLU-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
KToon is a 2D Animation Toolkit designed by animators (Toonka Films ) for
animators, focused to the Cartoon\'s industry.

%prep
%setup -q -n %{name}

%build
qmake ktoon.pro
%make

%install
rm -rf $RPM_BUILD_ROOT
install -m755 bin/%{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}

install -d $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} << EOF
?package(%{name}):command="%{name}" \
	icon="%{name}.png" \
	needs="x11" \
	section="Multimedia/Graphics" \
	title="K-Toon" \
	longtitle="%{Summary}"\
	xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=K-Toon
Comment=%{Summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Qt;KDE;X-MandrivaLinux-Multimedia-Graphics;Graphics
EOF


install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.txt
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_menudir}/%{name}
