%bcond debug 1

%if %{without debug}
%global debug_package %{nil}
%endif

%global srcname jellyfin-desktop
%global mpvqt 2ebbd38bf65d01be9c55d673ecd43c8bb9a6fc8e

Name:           jellyfin-desktop
Version:        2.0.0
Release:        1%{?dist}
Summary:        Jellyfin's official Desktop Client

# LICENSE does not use "or later" terminology
License:        GPL-2.0-only
URL:            https://github.com/jellyfin/%{srcname}
Source0:        %{url}/archive/v%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/jellyfin/jellyfin-desktop/master/resources/meta/org.jellyfin.JellyfinDesktop.appdata.xml

# binary build deps
BuildRequires:  cmake
BuildRequires:  g++
# BuildRequires:  wget
#BuildRequires:  unzip
#BuildRequires:  yasm

# Qt6 deps
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  qt6-qtwebengine-devel

# library deps
BuildRequires:  alsa-lib-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  fribidi-devel
BuildRequires:  gnutls-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  libcec-devel
BuildRequires:  libva-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libX11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mpv-devel
BuildRequires:  mpvqt-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  sdl2-compat-devel
BuildRequires:  uchardet-devel
BuildRequires:  zlib-ng-devel
# BuildRequires:  zlib-ng-compat-devel


%description
Jellyfin desktop client built with Qt WebEngine and libmpv.
Supports audio passthrough, hardware decoding, and playback of more formats
without transcoding.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_SKIP_RPATH=ON
%cmake_build


#check
#echo ">>>>>> check section <<<<<<<"
#echo $(pwd)
#ctest --output-on-failure


%install
%cmake_install

# the appdata in the tarball is outdated and was fixed 10 days after the release
install %{SOURCE1} %{buildroot}%{_datadir}/metainfo/org.jellyfin.JellyfinDesktop.appdata.xml


%files
%doc README.md
%license LICENSE
%{_bindir}/jellyfin-desktop
%{_datadir}/applications/org.jellyfin.JellyfinDesktop.desktop
%{_datadir}/metainfo/org.jellyfin.JellyfinDesktop.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/org.jellyfin.JellyfinDesktop.svg

%changelog
* Wed Feb 18 2026 Tarulia <mihawk.90+git@googlemail.com> - 2.0.0-1
- initial packaging
