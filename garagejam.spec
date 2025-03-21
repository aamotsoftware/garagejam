Name:           garagejam
Version:        5.0.0
Release:        1%{?dist}
Summary:        GarageJam is Music Studio Recording Software for GNOME
License:        GPLv3+
URL:            http://www.garagejam.org/
Source:         https://www.garagejam.org/src/%{name}-%{version}.tar.xz

BuildRequires:  gtk4-devel
BuildRequires:  pango
BuildRequires:  libchamplain-devel
BuildRequires:  libxml2-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  geoclue2-devel
BuildRequires:  geocode-glib-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-bad-free-devel
BuildRequires:  gstreamer1-plugins-base-devel
Requires:       gstreamer1 >= 1.8.3
Requires:       gstreamer1-plugins-ugly-free >= 1.8.3
Requires:       geoclue2-devel >= 2.5.7
Requires:       geocode-glib >= 3.20.1
Requires:       libshout-devel >= 2.4.3

%description
GarageJam is Music Studio Recording Software for GNOME

It supports immediate audio recording in compressed Ogg encoded audio
files stored in the $HOME/Music directory with XSPF 1.0 playlist from
the line input on a computer or remote audio cards through USB
connection through PipeWire with GStreamer with meta indexing on
https://api.gingerblue.org/

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
%find_lang %{name} --with-man

%check
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%post
%files -f %{name}.lang
%doc AUTHORS NEWS README TODO ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/garagejam.svg
%{_includedir}/%{name}
%{_metainfodir}/%{name}.appdata.xml

%changelog
* Fri Mar 14 2025 Ole Aamot <ole@aamot.org> - 5.0.0-0
- Development release

* Thu Jan 30 2025 Ole Aamot <ole@aamot.org> - 4.0.0-0
- Stable release with Recording and Playlist

* Thu Jan 30 2025 Ole Aamot <ole@aamot.org> - 3.0.0-0
- Development release

* Tue Jan 23 2024 Ole Aamot <ole@aamot.org> - 2.0.0-0
- Stable release with www.gingerblue.org/api/ Connect

* Wed Aug 16 2023 Ole Aamot <ole@aamot.org> - 1.0.0-0
- Initial Release

* Tue Aug 15 2023 Ole Aamot <ole@aamot.org> - 0.9.0-0
- Stable release with Connect, Recording and Playlist

* Mon Aug 07 2023 Ole Aamot <ole@aamot.org> - 0.8.0-0
- Stable release with Connect, Recording and Playback

* Mon Aug 07 2023 Ole Aamot <ole@aamot.org> - 0.7.0-0
- Experimental release with Connect friendly playlist

* Mon Aug 07 2023 Ole Aamot <ole@aamot.org> - 0.6.0-0
- Connect friendly release

* Mon Aug 07 2023 Ole Aamot <ole@aamot.org> - 0.5.0-0
- Experimental release

* Mon Aug 07 2023 Ole Aamot <ole@aamot.org> - 0.4.0-0
- Stable release

* Thu May 11 2023 Ole Aamot <ole@aamot.org> - 0.3.0-0
- Experimental release

* Mon May 01 2023 Ole Aamot <ole@aamot.org> - 0.2.0-0
- Development release

* Sun Apr 30 2023 Ole Aamot <ole@aamot.org> - 0.1.0-0
- Stable release

* Sun Apr 30 2023 Ole Aamot <ole@aamot.org> - 0.0.1-0
- GarageJam is Free Music Studio Recording Software for GNOME
