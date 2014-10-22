Name:       minidlna
Summary:    Ramdisk for booting root
Version:    1.1.4
Release:    1
Group:      Networking/Remote access
License:    GPLv2
Source0:    %{name}-%{version}.tar.gz
Source1:    minidlna.service

Requires:  libav
Requires:  libjpeg-turbo
Requires:  sqlite
Requires:  libexif
Requires:  libid3tag
Requires:  libogg
Requires:  libvorbis
Requires:  flac

BuildRequires:  gettext
BuildRequires:  libav-tools
BuildRequires:  libav-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  sqlite-devel
BuildRequires:  libexif-devel
BuildRequires:  libid3tag-devel
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  flac-devel

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}


%build
./autogen.sh
./configure --prefix=%{_prefix}
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
install -m 644 -D minidlna.conf %{buildroot}%{_sysconfdir}/minidlna.conf

install -D -m 644 %{SOURCE1} %{buildroot}/%{_lib}/systemd/system/minidlna.service
mkdir -p %{buildroot}/%{_lib}/systemd/system/multi-user.target.wants/
ln -s ../minidlna.service %{buildroot}/%{_lib}/systemd/system/multi-user.target.wants/


%files
%defattr(-,root,root,-)
%{_sbindir}/minidlnad
%{_datadir}/locale/*
%{_sysconfdir}/minidlna.conf

/%{_lib}/systemd/system/minidlna.service
/%{_lib}/systemd/system/multi-user.target.wants/minidlna.service

