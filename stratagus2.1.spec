%define name	stratagus2.1
%define	oname	stratagus
%define	version 2.1
%define rel	4
%define	release	%mkrel %{rel}

Name:		%{name} 
Summary:	A real time strategy game engine
Version:	%{version} 
Release:	%{release} 
Source0:	%{oname}-%{version}.tar.bz2
# http://bugs.debian.org/cgi-bin/bugreport.cgi?msg=10;filename=stratagus-2.1-flacapifix.diff;att=1;bug=427755
Patch0:		stratagus-2.1-flacapifix.diff
URL:		http://stratagus.sourceforge.net/
Group:		Games/Strategy
License:	GPL
BuildRequires:	libflac-devel
BuildRequires:	mesagl-devel
BuildRequires:	SDL-devel
BuildRequires:	bzip2-devel
BuildRequires:	imagemagick
BuildRequires:	lua5.0-devel
BuildRequires:	mad-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libpng-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{oname}-%{version}-%{release}-buildroot

%description
Stratagus is a free cross-platform real-time strategy gaming engine.
It includes support for playing over the internet/LAN, or playing a computer
opponent. The engine is configurable and can be used to create games with a
wide-range of features specific to your needs.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1

# lib64 fixes
perl -pi -e "s|/lib\b|/%{_lib}|g" configure*

%build

./configure --host=%{_host} --build=%{_build} \
    --target=%{_target_platform} \
    --program-prefix=%{?_program_prefix} \
    --prefix=%{_prefix} \
    --exec-prefix=%{_exec_prefix} \
    --bindir=%{_bindir} \
    --sbindir=%{_sbindir} \
    --sysconfdir=%{_sysconfdir} \
    --datadir=%{_datadir} \
    --includedir=%{_includedir} \
    --libdir=%{_libdir} \
    --libexecdir=%{_libexecdir} \
    --localstatedir=%{_localstatedir} \
    --sharedstatedir=%{_sharedstatedir} \
    --mandir=%{_mandir} \
    --infodir=%{_infodir} \
    --with-opengl \
    --with-x \
    --with-bzip2 \
    --with-ogg \
    --with-mikmod \
    --with-mad \
    --with-flac \
    --with-cdaudio=libcda \
    --with-lua=%{_prefix}

make

%install
rm -rf $RPM_BUILD_ROOT
install -m755 stratagus -D $RPM_BUILD_ROOT%{_gamesbindir}/%{name}
# Create and install icons
convert ./contrib/stratagus.ico -resize 32x32 ./stratagus-32.png
convert ./contrib/stratagus.ico -resize 48x48 ./stratagus-48.png
convert ./contrib/stratagus.ico -resize 16x16 ./stratagus-16.png
install -m644 stratagus-16.png -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 stratagus-32.png -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 stratagus-48.png -D %{buildroot}%{_liconsdir}/%{name}.png

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc README doc/*
%{_gamesbindir}/*
%{_iconsdir}/*

