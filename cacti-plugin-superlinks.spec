# TODO
# - use system fonts package for dejavu fonts
# - use system jquery package
%define		plugin	superlinks
%define		php_min_version 5.1.1
%include	/usr/lib/rpm/macros.php
Summary:	Plugin for Cacti - SuperLinks
Summary(pl.UTF-8):	Wtyczka do Cacti - SuperLinks (dodatkowe odnośniki)
Name:		cacti-plugin-%{plugin}
Version:	1.3
Release:	7
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/plugin:superlinks-v%{version}-1.tgz
# Source0-md5:	bed336cf2271d0e1159220e8e9624aa2
URL:		http://docs.cacti.net/plugin:superlinks
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	cacti
Requires:	cacti(pia) >= 2.9
Requires:	php(core) >= %{php_min_version}
Requires:	php(gd)
Requires:	php(mysql)
Requires:	php(pcre)
Requires:	php(session)
Requires:	php-date
Obsoletes:	cacti-plugin-links
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
Cacti plugin that allows the Cacti UI to be extended in ways that make
it easy for non plugin developers to use.

Features:
- It supports ANY number of extra tabs
- It will dynamically create the Tab graphics as pages are created
- It has the same user-based access-control as Weathermap
- It allows you to add new links to the Console menu as well as tabs
  and also blocks of content to the 'Welcome' front page.
- Allows you to directly embed another website/application without
  writing any HTML
- Allows you to modify the look of the login screen, to add your
  company's branding.
- It's also handy if you are a plugin developer, and need some tab
  graphics!

%description -l pl.UTF-8
To jest bardzo prosta wtyczka dla architektury wtyczek Cacti
stworzonej przez Jimmy'ego Smitha dla Cacti 0.8.x (0.9.0 ma mieć nowy
system wtyczek). Pozwala podpiąć dowolną liczbę stron HTML dowolnej
treści pod zakładki na górnej części strony lub jako dodatkowe wpisy w
menu Console. Wtyczki tej można używać do integracji innych narzędzi w
Cacti - w ten sposób można mieć w Cacti odnośniki do Smokepinga,
Request Trackera czy Nagiosa.

Wtyczka ma zastąpić wtyczkę Links tego samego autora, napisaną
wcześniej; ma następujące rozszerzenia:
- dowolną liczbę elementów zakładek/menu
- dla zakładek generowany jest obrazek w stylu Cacti, więc dodatkowe
  strony lepiej integrują się z Cacti
- wykorzystuje kod kontroli dostępu z Weathermap, więc zakładki mogą
  być widoczne tylko dla wybranych użytkowników
- oprócz zakładek jest możliwość tworzenia elementów menu Console oraz
  strony powitalnej
- można osadzać zewnętrzne strony bezpośrednio, bez pisania
  jakiegokolwiek HTML-a.

%prep
%setup -qc
%undos -f php,inc

mv %{plugin}/{README,COPYING} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
