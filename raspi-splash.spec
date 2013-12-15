Name:		raspi-splash
Version:	2.0
Release:	2.rpfr18
Summary:	Uses OpenGL to display an initial loading splash screen

Group:		Amusements/Graphics
License:	GPLv2+
Source0:	%{name}-%{version}.tgz

BuildRequires:  systemd-units
BuildRequires:	raspberrypi-vc-libs
BuildRequires:	raspberrypi-vc-libs-devel
BuildRequires:	raspberrypi-vc-static
#BuildRequires:	raspberrypi-vc-utils


%global systemdl %{_libdir}/systemd/system
%global systemde %{_sysconfdir}/systemd/system


%description
display an initial splash 
loading screen during boot for the user.


%prep

%setup -q

echo "setup"


%build
make

cat <<EOF > %{name}-helper
#!/bin/bash
%{_bindir}/%{name} & 
%{_bindir}/%{name}-stop &
EOF


cat <<EOF > %{name}-start.service
[Unit]
Description=Start Rasp Pi Boot Screen
DefaultDependencies=no
Before=systemd-vconsole-setup.service

[Service]
ExecStart=%{_bindir}/%{name}-helper
Type=forking

[Install]
WantedBy=sysinit.target
EOF


cat <<EOF > %{name}-stop
#!/bin/bash
while true
do
	proc=\`ps x | grep -E '(firstboot|login|Xorg)' | grep -v grep\`
	if [ "\$proc" != "" ]
	then
		/bin/systemctl stop %{name}-start.service
		break
	fi
	sleep 14
done
EOF


mv splash.bin %{name}

echo "build"


%install

install -d %{buildroot}/%{_bindir}
#mv pidora-logo-bgr.TGA %{buildroot}/%{_bindir}/
install -m 755 -p %{name} pidora-logo-bgr.TGA %{name}-helper %{name}-stop %{buildroot}/%{_bindir}/ 

install -d %{buildroot}/%{systemdl}
install -m 644 -p *.service %{buildroot}/%{systemdl}/

install -d %{buildroot}/%{systemde}/sysinit.target.wants
ln -s %{systemdl}/%{name}-start.service %{buildroot}/%{systemde}/sysinit.target.wants/

echo "install"

%files
%doc
%{_bindir}/*
%{systemdl}/*
%{systemde}/*


%post


%preun

%changelog
* Sat Dec 14 2013 Ai Dow <adow2@myseneca.ca> - 2.0-2.rpfr18
- Adding raspi.c and README file in the package

* Sat Nov 23 2013 Ai Dow <adow2@myseneca.ca> - 2.0-1.rpfr18
- Initial version 2.0 release

* Tue Nov 20 2012 Andrew Greene <andrew.greene@senecacollege.ca> - 1.0-1.rpfr18
- Updated package release tag for rpfr18

* Thu Oct 11 2012 Jon Chiappetta - 1.0-13.rpfr17
- New release build

* Sun Aug 26 2012 Jon Chiappetta <jonc_mailbox@yahoo.ca> - 1.0-12
- Fixed the stop script during multi & graphical modes

* Thu Aug 23 2012 Jon Chiappetta <jonc_mailbox@yahoo.ca> - 1.0-11
- Modified the splash stop service file

* Thu Aug 23 2012 Jon Chiappetta <jonc_mailbox@yahoo.ca> - 1.0-10
- Corrected the dist tag

* Thu Aug 23 2012 Jon Chiappetta <jonc_mailbox@yahoo.ca> - 1.0-9
- Cleaned up spec file

* Thu Aug 23 2012 Jon Chiappetta <jonc_mailbox@yahoo.ca> - 1.0-8
- Added a pre un-install script

* Thu Aug 23 2012 Jon Chiappetta <jonc_mailbox@yahoo.ca> - 1.0-7
- Hid the zlib libz libraries

* Fri Aug 17 2012 Jon Chiappetta <jonc_mailbox@yahoo.ca> - 1.0-6
- Converted back to the gif version plus zlib c lib

* Thu Aug 09 2012 Jon Chiappetta <jonc_mailbox@yahoo.ca> - 1.0-5
- Fixed up the generated systemd service files

* Wed Aug 08 2012 Jon Chiappetta <jonc_mailbox@yahoo.ca> - 1.0-4
- Simpler version with only one 2d rotating image

* Tue Jul 24 2012 Jon Chiappetta <jonc_mailbox@yahoo.ca> - 1.0-3
- New logo rendering

* Mon Jul 16 2012 Jon Chiappetta <jonc_mailbox@yahoo.ca> - 1.0-2
- Initial packaging and release
