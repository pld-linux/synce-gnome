# TODO
# - update pl
Summary:	GNOME Systray applet for inputing device password
Summary(pl.UTF-8):	Interfejs GNOME
Name:		synce-gnome
Version:	0.11
Release:	3
License:	MIT
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	e79f5d43fefe30b51edc8750fe451a2d
URL:		http://www.synce.org/
BuildRequires:	python
BuildRequires:	python-setuptools
Requires:	notification-daemon
Requires:	python-dbus
Requires:	python-pygtk-gtk
Requires:	python-pynotify
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SynCE-GNOME displays nice libnotify messages when a device is connected or
disconnected, and it prompts for a password if one is required.

Note: Despite this being called synce-gnome, this is not
GNOME-specific.

%description -l pl.UTF-8
Interfejs GNOME.

Uwaga: mimo nazwy synce-gnome, nie jest on specyficzny dla GNOME.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/synce-gnome
%{py_sitescriptdir}/*.egg-info
