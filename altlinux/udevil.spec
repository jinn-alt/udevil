Name: udevil
Version: 0.4.4
Release: alt0.1

Summary: Command line program which mounts and unmounts removable devices
License: GPL-3.0+
Group: File tools
Url: https://github.com/IgnorantGuru/udevil

Source0: %name-%version.tar
Patch0: %name-%version-alt-specific.patch

BuildPreReq: intltool glib2-devel libudev-devel

%description
Mounts and unmounts removable devices and networks without a password (set
suid), shows device info, monitors device changes.  Emulates mount's and
udisks's command line usage and udisks v1's output.  Includes the devmon
automounting daemon.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure
%make

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%dir %_sysconfdir/%name
%_sysconfdir/%name/*
%_sysconfdir/sysconfig/*
/lib/systemd/system/*
%_bindir/*
%doc AUTHORS ChangeLog README

%changelog
* Sun Oct 18 2015 Dmitriy Khanzhin <jinn@altlinux.org> 0.4.4-alt0.1
- 0.4.4

* Mon Apr 27 2015 Dmitriy Khanzhin <jinn@altlinux.org> 0.4.3-alt0.M70T.0.1
- initial build for AltLinux
