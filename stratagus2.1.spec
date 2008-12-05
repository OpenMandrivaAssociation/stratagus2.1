%define name	stratagus2.1
%define	oname	stratagus
%define	version 2.1
%define rel	2
%define	release	%mkrel %{rel}

Name:		%{name} 
Summary:	A real time strategy game engine
Version:	%{version} 
Release:	%{release} 
Source0:	%{oname}-%{version}.tar.bz2
URL:		http://stratagus.sourceforge.net/
Group:		Games/Strategy
BuildRoot:	%{_tmppath}/%{oname}-%{version}-%{release}-buildroot
License:	GPL
BuildRequires:	SDL-devel bzip2-devel oggvorbis-devel libmikmod-devel X11-devel
BuildRequires:	mad-devel libcdaudio-devel lua5.0-devel libflac-devel

%description
Stratagus is a free cross-platform real-time strategy gaming engine.
It includes support for playing over the internet/LAN, or playing a computer
opponent. The engine is configurable and can be used to create games with a
wide-range of features specific to your needs.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure	--with-opengl \
		--with-x \
		--with-bzip2 \
		--with-ogg \
		--with-mikmod \
		--with-mad \
		--with-flac \
		--with-cdaudio=libcda \
		EXTRA_CFLAGS="$RPM_OPT_FLAGS"

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

