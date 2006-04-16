%define		vendor_name kglwatersaver
Summary:	KGLWaterSaver - OpenGL screensaver for KDE
Name:		kde-screensaver-%{vendor_name}
Version:	0.6
Release:	0.1
License:	GPL
Group:		X11/Amusements
Source0:	http://kwatersaver.c0n.de/downloads/%{vendor_name}-%{version}.tar.bz2
# Source0-md5:	b7a9bc4cba43cef57a0459f186fb3980
URL:		http://kwatersaver.c0n.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	kdebase-screensavers
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Screensaver for KDE using OpenGL for visual effects.
Features:
- Choose between Images or the current Desktop to "sink under water"
- Various effects: Whirl, Bubble, Rain

%prep
%setup -q -n %{vendor_name}-%{version}

%build
cp -f /usr/share/automake/config.sub admin
# autokaka generation fails (too old admin/ dir?), but luckily we don't need it now
#%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kscreensaver

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	desktopdir=%{_datadir}/apps/kscreensaver

%find_lang %{vendor_name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{vendor_name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kglwatersaver.kss
%{_datadir}/apps/kscreensaver/kglwatersaver.desktop
