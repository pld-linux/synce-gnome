Summary:	GNOME Systray applet for inputing device password
Summary(pl.UTF-8):	Aplet tacki systemowej GNOME do wprowadzania haseł urządzeń
Name:		synce-gnome
Version:	0.11
Release:	5
License:	MIT
Group:		Applications/Communications
Source0:	http://downloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	e79f5d43fefe30b51edc8750fe451a2d
URL:		http://www.synce.org/
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
Requires:	dbus(org.freedesktop.Notifications)
Requires:	python-dbus
Requires:	python-pygtk-gtk
Requires:	python-pynotify
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SynCE-GNOME displays nice libnotify messages when a device is
connected or disconnected, and it prompts for a password if one is
required.

Note: Despite this being called synce-gnome, this is not
GNOME-specific.

%description -l pl.UTF-8
SynCE-GNOME wyświetla ładne komunikaty libnotify przy podłączaniu lub
odłączaniu urządzenia oraz pyta o hasło, kiedy jest wymagane.

Uwaga: mimo nazwy synce-gnome, aplet nie jest on specyficzny dla
GNOME.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/synce-gnome
%{py_sitescriptdir}/*.egg-info
