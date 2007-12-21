Summary:	GNOME UI
Summary(pl.UTF-8):	Interfejs GNOME
Name:		synce-gnome
Version:	0.10.0
Release:	3
License:	MIT
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	d7da61dbb06ad5206bc65c599be938d4
URL:		http://www.synce.org/
BuildRequires:	sed >= 4.0
Requires:	notification-daemon
Requires:	python-dbus
Requires:	python-pygtk-gtk
Requires:	python-pynotify
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME UI.

Note: Despite this being called synce-gnome, this is not
GNOME-specific.

%description -l pl.UTF-8
Interfejs GNOME.

Uwaga: mimo nazwy synce-gnome, nie jest on specyficzny dla GNOME.

%prep
%setup -q
%{__sed} -i -e '1s,^#!.*python,#!%{__python},' src/test.py

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install src/test.py $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/synce-gnome
